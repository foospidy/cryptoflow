"""
Buy The Dip module
"""
import os
import pprint
import cbpro
import gemini

from airflow.models import Variable

from cryptoflow import bittrex
from cryptoflow.slack import slack_webhook


class BuyTheDip():
    """
    Buy The Dip class
    """
    exchanges = []
    asset = None
    price = None
    use = 'last'
    coinbasepro = None
    gemini = None
    bittrex = None
    uphold = None

    def __init__(self, asset=None, price=None, use='last'):
        self.exchanges = self._configured_exchanges()
        self.asset = asset.upper()
        self.price = price
        self.use = use

        # Initialize clients for configured exchanges
        if "coinbasepro" in self.exchanges:
            self.coinbasepro = cbpro.AuthenticatedClient(Variable.get('COINBASEPRO_KEY'),
                                                    Variable.get('COINBASEPRO_SECRET'),
                                                    Variable.get('COINBASEPRO_PASSPHRASE'))
        if "gemini" in self.exchanges:
            self.gemini = gemini.PrivateClient(Variable.get('GEMINI_KEY'),
                                            Variable.get('GEMINI_SECRET'))
        if "bittrex" in self.exchanges:
            self.bittrex = bittrex.Bittrex3(Variable.get('BITTREX_KEY'),
                                            Variable.get('BITTREX_SECRET'))
        if "uphold" in self.exchanges:
            # tbd
            pass

    @staticmethod
    def _configured_exchanges():
        exchanges = []

        # pylint: disable=bare-except
        try:
            Variable.get("COINBASEPRO_KEY")
            exchanges.append("coinbasepro")
        except:
            pass

        # pylint: disable=bare-except
        try:
            Variable.get("GEMINI_KEY")
            exchanges.append("gemini")
        except:
            pass

        # pylint: disable=bare-except
        try:
            Variable.get("BITTREX_KEY")
            exchanges.append("bittrex")
        except:
            pass

        # pylint: disable=bare-except
        try:
            Variable.get("UPHOLD_KEY")
            exchanges.append("uphold")
        except:
            pass

        return exchanges

    def get_best_price(self):
        """ Get the best price available """
        # pylint: disable=too-many-branches,too-many-statements
        best = {}
        prices_ask = {}
        prices_last = {}

        if self.coinbasepro is not None:
            cbpr = self.coinbasepro.get_product_ticker("{}-USD".format(self.asset))

            if "message" in cbpr:
                cbpr["price"] = cbpr["message"]
                cbpr["bid"] = cbpr["message"]
                cbpr["ask"] = cbpr["message"]
            else:
                prices_ask["coinbasepro"] = cbpr["ask"]
                prices_last["coinbasepro"] = cbpr["price"]

            print("COINBASE:\t{} - bid: {} ask: {}".format(cbpr["price"], cbpr["bid"], cbpr["ask"]))

        if self.gemini is not None:
            gemr = self.gemini.get_ticker("{}USD".format(self.asset))

            if "message" in gemr:
                gemr["last"] = gemr["result"]
                gemr["bid"] = gemr["reason"]
                gemr["ask"] = gemr["message"]
            else:
                prices_ask["gemini"] = gemr["ask"]
                # Gemini needs the ask, instead of last, otherwise order won't fill
                prices_last["gemini"] = gemr["ask"]

            print("GEMINI: \t{} - bid: {} ask: {}".format(gemr["last"], gemr["bid"], gemr["ask"]))

        if self.bittrex is not None:
            asset = "{}-USD".format(self.asset)
            bitr = self.bittrex.get_ticker(asset)

            if "code" in bitr:
                bitr["lastTradeRate"] = bitr["code"]
                bitr["bidRate"] = bitr["code"]
                bitr["askRate"] = bitr["code"]
            else:
                prices_ask["bittrex"] = bitr["askRate"]
                prices_last["bittrex"] = bitr["lastTradeRate"]

            print("BITTREX: \t{} - bid: {} ask: {}".format(bitr["lastTradeRate"],
                                                           bitr["bidRate"],
                                                           bitr["askRate"]))

        if self.uphold is not None:
            pass

        min_ask = {}
        min_last = {}

        prices_ask_len = len(prices_ask)
        if prices_ask_len > 0:
            min_ask = min(zip(prices_ask.values(), prices_ask.keys()))

        if self.use == 'ask':
            best["price"] = float(min_ask[0])
            best["exchange"] = min_ask[1]

        prices_last_len = len(prices_last)
        if prices_last_len > 0:
            min_last = min(zip(prices_last.values(), prices_last.keys()))

        min_last_len = len(min_last)
        if self.use == 'last' and min_last_len > 0:
            best["price"] = float(min_last[0])
            best["exchange"] = min_last[1]

        print("Best price {}".format(best))
        return best

    def buy_dip(self, best=None, spend=None, smallest_unit=8):
        """
        Buy the dip!
        """
        response = {}
        order_success = True
        order_message = None

        # get size based on spend limit and best price
        size = round(float(spend) / float(best['price']), smallest_unit)

        buy_message = "{} limit order at {} of size {} on {}.".format(self.asset,
                                                                      best['price'],
                                                                      size,
                                                                      best['exchange'])
        print(buy_message)

        if best['exchange'] == "coinbasepro":
            response = self.coinbasepro.place_order("{}-USD".format(self.asset),
                                                    "buy",
                                                    "limit",
                                                    price=best['price'],
                                                    size=size)
            if "message" in response:
                order_success = False
                order_message = response['message']

        elif best['exchange'] == "gemini":
            response = self.gemini.new_order("{}USD".format(self.asset),
                                             str(size),
                                             str(best['price']),
                                             "buy")
            if "is_cancelled" in response and response['is_cancelled'] is True:
                order_success = False
                order_message = response

            if "message" in response:
                order_success = False
                order_message = response

        elif best['exchange'] == "bittrex":
            response = self.bittrex.place_limit_order("{}-USD".format(self.asset),
                                                      best['price'],
                                                      size)
            if "code" in response:
                order_success = False
                order_message = response

        if order_success:
            # Create order file
            buy_the_dip_dir = "{}/.buythedip".format(os.environ['HOME'])
            if not os.path.exists(buy_the_dip_dir):
                os.mkdir(buy_the_dip_dir)

            with open("{}/{}_{}_{}".format(buy_the_dip_dir,
                                           best['exchange'],
                                           self.asset,
                                           response['id']), 'w') as order_file:
                order_file.write(str(best['price']) + "\n")

            # pprint full response
            pprint.pprint(response)

            # Send buy_message to slack if webhook configured
            slack_webhook(buy_message)

        response['success'] = order_success
        response['message'] = order_message

        return response

class CheckOrders():
    """
    Check orders class
    """
    def __init__(self):
        self.buy_the_dip_dir = "{}/.buythedip".format(os.environ['HOME'])
        self.coinbasepro = cbpro.AuthenticatedClient(Variable.get('COINBASEPRO_KEY'),
                                                  Variable.get('COINBASEPRO_SECRET'),
                                                  Variable.get('COINBASEPRO_PASSPHRASE'))
        self.gemini = gemini.PrivateClient(Variable.get('GEMINI_KEY'),
                                           Variable.get('GEMINI_SECRET'))

    def print_orders(self):
        """
        Print pending orders
        """
        orders = os.listdir(self.buy_the_dip_dir)
        for order in orders:
            print(order)

    def check_status(self):
        """
        Check order status
        """
        orders = os.listdir(self.buy_the_dip_dir)

        for order in orders:
            order_parts = order.split("_")

            if order_parts[0] == "coinbasepro":
                settled = False
                status = self.coinbasepro.get_order(order_parts[2])
                settled = status['settled']

            if order_parts[0] == "gemini":
                status = self.gemini.status_of_order(order_parts[2])
                settled = False

                if "is_live" in status and status['is_live'] is False:
                    settled = True

            status_message = "{} on {} - filled ({})".format(order_parts[1],
                                                             order_parts[0],
                                                             settled)
            print(status_message)

            if settled:
                # Send slack message if configured
                slack_webhook(status_message)
                # Delete order files for settled orders
                os.remove("{}/{}".format(self.buy_the_dip_dir, order))
