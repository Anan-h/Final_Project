import os

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APICards:
    END_POINT = "/cards"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(base_dir, '../../config.json')
    secret_file_path = os.path.join(base_dir, '../../secret.json')

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        self.secret = ConfigProvider().load_from_file(self.secret_file_path)
        self.API_KEY = self.secret['trello_api_key']
        self.API_TOKEN = self.secret['trello_api_token']

    def create_new_card_on_list(self, list_id, card_name):
        """
        send an api request to create new card into list
        :param list_id: the id of the desired list
        :param card_name: the name of the card that is going to create
        :return: response wrapper
        """
        params = {
            "idList": list_id,
            "key": self.API_KEY,
            "token": self.API_TOKEN,
            "name": card_name
        }
        full_url = f"{self.config['api_base_url']}{self.END_POINT}"
        header = self.config['header']
        return self._request.post_request(url=full_url, headers=header, params=params)
