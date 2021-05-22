"""
Bittrex APIv3 helper module
"""
import hashlib
import hmac
import time
import json
import requests


API_URL = "https://api.bittrex.com/v3"

class Bittrex3():
    """
    Bittrex APIv3
    """
    def __init__(self, key, secret):
        self.api_key = key
        self.api_secret = secret

    @staticmethod
    def _get_nonce():
        return int(time.time() * 1000)

    @staticmethod
    def _get_digest(message):
        return hashlib.sha512(message.encode()).hexdigest()

    @staticmethod
    def _get_signature(message, salt):
        return hmac.new(salt.encode(), message.encode(), hashlib.sha512).hexdigest()

    def call_bittrex(self, method="GET", endpoint=None, body=""):
        """
        Make a call to the Bittrex API with authentication
        """
        nonce = str(self._get_nonce())
        digest = self._get_digest(body)
        # [timestamp, uri, method, contentHash, subaccountId].join('')
        signature_payload = "{}{}{}{}{}".format(nonce,
                                                "{}{}".format(API_URL, endpoint),
                                                method,
                                                digest,
                                                "")

        headers = {
            "Content-Type": "application/json",
            "Api-Key": self.api_key,
            "Api-Timestamp": nonce,
            "Api-Content-Hash": digest,
            "Api-Signature": self._get_signature(signature_payload, self.api_secret)
        }

        if method == "GET":
            response = requests.get("{}{}".format(API_URL, endpoint),
                                    headers=headers)

        if method == "POST":
            response = requests.post("{}{}".format(API_URL, endpoint),
                                     headers=headers,
                                     data=body)

        return response.json()

    def get_ticker(self, asset):
        """
        Get ticker info
        """
        return self.call_bittrex(method="GET",
                                 endpoint="/markets/{}/ticker".format(asset))

    def place_limit_order(self, asset, price, size):
        """
        Place a limit order
        {
            "marketSymbol": "string",
            "direction": "string",
            "type": "LIMIT",
            "quantity": "number (double)",
            "limit": "number (double)",
            "timeInForce": "GOOD_TIL_CANCELLED || IMMEDIATE_OR_CANCEL"
                           " || FILL_OR_KILL || POST_ONLY_GOOD_TIL_CANCELLED",
        }
        """
        payload = {
            "marketSymbol": asset,
            "direction": "BUY",
            "type": "LIMIT",
            "quantity": size,
            "limit": price,
            "timeInForce": "GOOD_TIL_CANCELLED"
        }

        return self.call_bittrex(method="POST",
                                 endpoint="/orders",
                                 body=json.dumps(payload))
