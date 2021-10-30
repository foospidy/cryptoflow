"""
Buy The Dip module
"""
import os
import pprint
import cbpro
import gemini

from airflow.models import Variable

from cryptoflow.config import configured_exchanges
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

    def __init__(self, asset=None, price=None, use='last'):
        self.exchanges = configured_exchanges()
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

    def get_best_price(self):
        """ Get the best price available """
        # pylint: disable=too-many-branches,too-many-statements
        best = {}
        prices_ask = {}
        prices_last = {}

        if self.coinbasepro is not None:
            cbpr = self.coinbasepro.get_product_ticker(f"{self.asset}-USD")

            if "message" in cbpr:
                cbpr["price"] = cbpr["message"]
                cbpr["bid"] = cbpr["message"]
                cbpr["ask"] = cbpr["message"]
            else:
                prices_ask["coinbasepro"] = cbpr["ask"]
                prices_last["coinbasepro"] = cbpr["price"]

            print(f'COINBASE:\t{cbpr["price"]} - bid: {cbpr["bid"]} ask: {cbpr["ask"]}')

        if self.gemini is not None:
            gemr = self.gemini.get_ticker(f"{self.asset}USD")

            if "message" in gemr:
                gemr["last"] = gemr["result"]
                gemr["bid"] = gemr["reason"]
                gemr["ask"] = gemr["message"]
            else:
                if gemr["ask"] is not None: # can be None in rare cases
                    prices_ask["gemini"] = gemr["ask"]
                    # Gemini needs the ask, instead of last, otherwise order won't fill
                    prices_last["gemini"] = gemr["ask"]

            print(f'GEMINI: \t{gemr["last"]} - bid: {gemr["bid"]} ask: {gemr["ask"]}')

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

        print(f"Best price {best}")
        return best

    def buy_dip(self, best=None, spend=None, smallest_unit=8):
        """
        Buy the dip!
        """
        order_response = {}
        order_success = True
        order_reason = None
        order_message = None

        # get size based on spend limit and best price
        size = round(float(spend) / float(best['price']), smallest_unit)

        # pylint: disable=line-too-long
        buy_message = f"{self.asset} limit order at {best['price']} of size {size} on {best['exchange']}."
        print(buy_message)

        if best['exchange'] == "coinbasepro":
            response = self.coinbasepro.place_order(f"{self.asset}-USD",
                                                    "buy",
                                                    "limit",
                                                    price=best['price'],
                                                    size=size)
            if "message" in response:
                order_success = False
                order_message = response['message']

        elif best['exchange'] == "gemini":
            response = self.gemini.new_order(f"{self.asset}USD",
                                             str(size),
                                             str(best['price']),
                                             "buy")

            if "result" in response and response['result'] == "error":
                order_success = False
                order_reason = response['reason']
                order_message = response['message']

        if order_success:
            # Create order file
            buy_the_dip_dir = f"{os.environ['HOME']}/.buythedip"
            if not os.path.exists(buy_the_dip_dir):
                os.mkdir(buy_the_dip_dir)

            order_file_path = f"{buy_the_dip_dir}/{best['exchange']}_{self.asset}_{response['id']}"
            with open(order_file_path, "w", encoding='utf-8') as order_file:
                order_file.write(str(best['price']) + "\n")

            # pprint full response
            pprint.pprint(response)

            # Send buy_message to slack if webhook configured
            slack_webhook(buy_message)

        order_response['success'] = order_success
        order_response['reason'] = order_reason
        order_response['message'] = order_message

        return order_response

class CheckOrders():
    """
    Check orders class
    """
    def __init__(self):
        self.buy_the_dip_dir = f"{os.environ['HOME']}/.buythedip"
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
                settled = status.get("settled", False)

            if order_parts[0] == "gemini":
                status = self.gemini.status_of_order(order_parts[2])
                settled = False

                if "is_live" in status and status['is_live'] is False:
                    settled = True

            status_message = f"{order_parts[1]} on {order_parts[0]} - filled"
            print(status_message)

            if settled:
                # Send slack message if configured
                slack_webhook(status_message)
                # Delete order files for settled orders
                os.remove(f"{self.buy_the_dip_dir}/{order}")
