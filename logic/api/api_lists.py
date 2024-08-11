import os

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APILists:
    END_POINT = "/lists/"
    config = ConfigProvider().load_from_file('../../config.json', __file__)
    secret = ConfigProvider().load_from_file('../../secret.json', __file__)

    def __init__(self, request: APIWrapper):
        self._request = request
        self.API_KEY = self.secret['trello_api_key']
        self.API_TOKEN = self.secret['trello_api_token']

    def get_cards_ids_from_list_by_id(self, list_id):
        """
        send an api request to get the ids of all cards located in list
        :param list_id: the id of the desired list
        :return: all the cards ids in the list
        """
        full_url = f"{self.config['api_base_url']}{self.END_POINT}{list_id}/cards"
        params = {
            "key": self.API_KEY,
            "token": self.API_TOKEN
        }
        header = self.config['header']
        response = self._request.get_request(url=full_url, params=params, headers=header)
        data = response.data
        card_ids = []
        for i in range(len(data)):
            card_ids.append(data[i]['id'])
        return card_ids

    def move_all_cards_from_list_to_list(self, from_list_id, to_list_id, board_id):
        """
        send an api request to move all cards from list to list
        :param from_list_id: the id of the list that the cards located at
        :param to_list_id: the id of the list that the cards going to move for
        :param board_id: the id of the board that include the lists
        :return: response wrapper
        """
        full_url = f"{self.config['api_base_url']}{self.END_POINT}{from_list_id}/moveAllCards"
        params = {
            "idBoard": board_id,
            "idList": to_list_id,
            "key": self.API_KEY,
            "token": self.API_TOKEN
        }
        return self._request.post_request(url=full_url, params=params)


