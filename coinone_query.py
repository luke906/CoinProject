import base64
import simplejson as json
import hashlib
import hmac
import httplib2
import time

ACCESS_TOKEN = '48fd6387-7fb9-4976-9a87-6c8607f3d148'
SECRET_KEY = 'dac350be-520d-4608-9fab-91c32ae3109f'

PAYLOAD = {
  "access_token": ACCESS_TOKEN,
}

def get_encoded_payload(payload):
    payload[u'nonce'] = int(time.time()*1000)

    dumped_json = json.dumps(payload)
    encoded_json = base64.b64encode(dumped_json.encode())
    return encoded_json

def get_signature(encoded_payload, secret_key):
    secret_key_byte = str(secret_key).upper().encode()
    signature = hmac.new(secret_key_byte, encoded_payload, hashlib.sha512)
    return signature.hexdigest()

def get_response(payload, action=None):

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

    encoded_payload = get_encoded_payload(payload)
    headers = {
        'Content-type': 'application/json',
        'X-COINONE-PAYLOAD': encoded_payload,
        'X-COINONE-SIGNATURE': get_signature(encoded_payload, SECRET_KEY)
    }
    http = httplib2.Http()
    response, content = http.request(URL, 'POST', headers=headers, body=encoded_payload)
    return content

def get_result(action):
    content = get_response(PAYLOAD, action)
    content = json.loads(content)

    return content

if __name__   == "__main__":
    print(get_result('Balance'))
    print("\n")
    print(get_result('Daily Balance'))
    print("\n")
    print(get_result('Deposit Address'))
    print("\n")
    print(get_result('User Information'))
    print("\n")
    print(get_result('Virtual Account'))
    print("\n")