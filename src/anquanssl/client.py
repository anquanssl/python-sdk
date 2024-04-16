import requests
import uuid
import datetime
import hashlib
import hmac
import base64
import json
from urllib.parse import urlencode, urlparse


ORIGIN_API = "https://api.orion.pki.plus/api/v1"

def sign(base_string, access_key_secret):
    # print ("basestring", base_string)
    '''
    print("debug ", hmac.new(
        bytes(access_key_secret, 'utf-8'),
          bytes(base_string, 'utf-8'),
          hashlib.sha256
          ).hexdigest())
    print("debug", base64.b64encode(hmac.new(
        bytes(access_key_secret, 'utf-8'),
        bytes(base_string, 'utf-8'),
        hashlib.sha256
    ).digest()).decode('utf-8'))
    '''

    return base64.b64encode(hmac.new(
        bytes(access_key_secret, 'utf-8'),
        bytes(base_string, 'utf-8'),
        hashlib.sha256
    ).digest()).decode('utf-8')


class Client:
    def __init__(self, access_key_id, access_key_secret, api_origin: str = None, connect_timeout=5, read_timeout=15):
        self.api_origin = ORIGIN_API
        if api_origin is not None:
            self.api_origin = api_origin
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
    
    def get(self, uri: str, query: dict = {}, body: dict = {}):
        return self.call("GET", uri, query, body)

    def post(self, uri: str, query: dict = {}, body: dict = {}):
        return self.call("POST", uri, query, body)

    def call(self, method: str, uri: str, query: dict, body: dict):
        query = list(query.items())
        query.append(('accessKeyId', self.access_key_id))
        query.append(('nonce', ''.join(str(uuid.uuid1()).split('-'))));
        query.append(('timestamp', datetime.datetime.now().replace(microsecond=0).isoformat() + "Z"))
        query.sort()

        parameters = [(k, v) for k, v in query]

        for item in body.items():
            if isinstance(item[1], dict):
                for key, value in item[1].items():
                    parameters.append((item[0] + "[" + key + "]", value))
            else:
                parameters.append(item)
        parameters.sort()

        url = self.api_origin + uri + '?' + urlencode(query)
        # print("=== call debug ===")
        signature = sign(urlparse(url).path + '?' + urlencode(parameters), self.access_key_secret)
        query.append(("sign", signature))
        query.sort()
        url = self.api_origin + uri + '?' + urlencode(query)

        response = requests.request(method, url, data=json.dumps(body), headers={"Content-Type": "application/json"})
        # print("url:", url)
        # print("body:", body)
        # print("=== call debug end ===\n")
        return response.json()
