import base64
import json
import hashlib
import hmac
import requests
import time


class CoinoneAPIManager(object):
    def __init__(self):
        self.ACCESS_TOKEN = '48fd6387-7fb9-4976-9a87-6c8607f3d148'
        self.SECRET_KEY = 'dac350be-520d-4608-9fab-91c32ae3109f'
        self.PAYLOAD = {"access_token": self.ACCESS_TOKEN,}

    def get_encoded_payload(self, payload):
        payload[u'nonce'] = int(time.time() * 1000)

        dumped_json = json.dumps(payload)
        encoded_json = base64.b64encode(dumped_json.encode())
        return encoded_json

    def get_signature(self, encoded_payload, secret_key):
        signature = hmac.new(str(secret_key).upper().encode(), encoded_payload, hashlib.sha512)
        return signature.hexdigest()

    def get_response(self, payload, action):

        URL = 'https://api.coinone.co.kr/v2/account/balance/'

        if action == "Balance":
            URL = 'https://api.coinone.co.kr/v2/account/balance/'
        elif action == "Daily Balance":
            URL = 'https://api.coinone.co.kr/v2/account/daily_balance/'
        elif action == "Deposit Address":
            URL = 'https://api.coinone.co.kr/v2/account/deposit_address/'
        elif action == "User Information":
            URL = 'https://api.coinone.co.kr/v2/account/user_info/'
        elif action == "Virtual Account":
            URL = 'https://api.coinone.co.kr/v2/account/virtual_account/'

        encoded_payload = self.get_encoded_payload(payload)
        headers = {
            'Content-type': 'application/json',
            'X-COINONE-PAYLOAD': encoded_payload,
            'X-COINONE-SIGNATURE': self.get_signature(encoded_payload, self.SECRET_KEY)
        }

        content = requests.post(URL, data=encoded_payload, headers=headers)
        return content

    def get_result(self, action):
        response = self.get_response(self.PAYLOAD, action)
        content = response.json()

        return content