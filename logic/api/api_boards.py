import os

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIBoards:
    END_POINT = "/boards"
    config = ConfigProvider().load_from_file('../../config.json')
    secret = ConfigProvider().load_from_file('../../secret.json')
    API_KEY = secret['trello_api_key']
    API_TOKEN = secret['trello_api_token']

    def __init__(self, request: APIWrapper):
        self._request = request

    def create_new_board(self, name):
        """
        send an api request to create a new board
        :param name: name for the board
        :return: response wrapper
        """
        params = {
            "name": name,
            "key": self.API_KEY,
            "token": self.API_TOKEN

        }

        url = f"{self.config['api_base_url']}{self.END_POINT}"
        return self._request.post_request(url, params=params)

    def delete_board_by_id(self, board_id):
        """
        send an api request to delete a board by board_id
        :param board_id: the id of the board
        :return: response wrapper
        """
        params = {
            "key": self.API_KEY,
            "token": self.API_TOKEN
        }

        url = f"{self.config['api_base_url']}{self.END_POINT}/{board_id}"
        return self._request.delete_request(url, params=params)

    def get_to_do_list_id_by_board_id(self, board_id):
        """
        send an api request to get the id of the To-Do list by the board_id
        :param board_id: the id of the board that the list present in
        :return: the id of the To-Do list
        """
        params = {
            "key": self.API_KEY,
            "token": self.API_TOKEN
        }
        url = f"{self.config['api_base_url']}{self.END_POINT}/{board_id}/lists"
        response = self._request.get_request(url, params=params)
        to_do_list_id = response.data[0]['id']
        return to_do_list_id

    def get_done_list_id_by_board_id(self, board_id):
        """
        send an api request to get the id of the Done list by the board_id
        :param board_id: the id of the board that the list present in
        :return: the id of the Done list
        """
        params = {
            "key": self.API_KEY,
            "token": self.API_TOKEN
        }
        url = f"{self.config['api_base_url']}{self.END_POINT}/{board_id}/lists"
        response = self._request.get_request(url, params=params)
        to_do_list_id = response.data[2]['id']
        return to_do_list_id

    def update_board_name_by_board_id(self, board_id, new_name):
        """
        send an api request to update board name
        :param board_id: the id of the board to change the name for
        :param new_name: the new name
        :return: response wrapper
        """
        full_url = f"{self.config['api_base_url']}{self.END_POINT}/{board_id}"
        params = {
            "name": new_name,
            "key": self.API_KEY,
            "token": self.API_TOKEN
        }
        return self._request.put_request(url=full_url, params=params)

    def add_member_to_board(self, board_id, member_id, member_type):
        """
        send an api request to add member into board
        :param board_id: the desired board id
        :param member_id: the desired member id
        :param member_type: the type of the member {admin,normal}
        :return: response wrapper
        """
        full_url = f"{self.config['api_base_url']}{self.END_POINT}/{board_id}/members/{member_id}"
        params = {
            'type': member_type,
            "key": self.API_KEY,
            "token": self.API_TOKEN
        }
        return self._request.put_request(url=full_url, params=params)

    def remove_member_from_board(self, board_id, member_id):
        """
        send an api request to remove member from board
        :param board_id: the desired board id
        :param member_id: the desired member id
        :return: response wrapper
        """
        full_url = f"{self.config['api_base_url']}{self.END_POINT}/{board_id}/members/{member_id}"
        params = {
            "key": self.API_KEY,
            "token": self.API_TOKEN
        }
        return self._request.delete_request(url=full_url, params=params)
