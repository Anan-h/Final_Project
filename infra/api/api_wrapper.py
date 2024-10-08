import requests
from infra.logger import Logger
from infra.api.response_wrapper import ResponseWrapper


class APIWrapper:

    def __init__(self):
        self._request = None

    def get_request(self, url, body=None, headers=None, params=None):
        response = requests.get(url=url, json=body, headers=headers, params=params)
        return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())

    def post_request(self, url, body=None, headers=None, params=None):
        response = requests.post(url=url, json=body, headers=headers, params=params)
        return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())

    def put_request(self, url, body=None, headers=None, params=None):
        response = requests.put(url=url, json=body, headers=headers, params=params)
        return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())

    def delete_request(self, url, body=None, headers=None, params=None):
        response = requests.delete(url=url, json=body, headers=headers, params=params)
        return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())