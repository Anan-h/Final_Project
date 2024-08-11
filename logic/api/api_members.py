import os
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIMembers:
    END_POINT = "/members/"
    config = ConfigProvider().load_from_file('../../config.json', __file__)
    secret = ConfigProvider().load_from_file('../../secret.json', __file__)

    def __init__(self, request: APIWrapper):
        self._request = request
        self.API_KEY = self.secret['trello_api_key']
        self.API_TOKEN = self.secret['trello_api_token']

    def get_member_id_by_user_name(self, user_name):
        """
        send an api request to get the id of certain user based on the username
        :param user_name: name of the user as registered
        :return: the id of the desired user
        """
        api_key = self.secret['trello_api_key']
        api_token = self.secret['trello_api_token']
        full_url = f"{self.config['api_base_url']}{self.END_POINT}{user_name}"
        params = {
            'key': api_key,
            'token': api_token
        }
        response = self._request.get_request(url=full_url, headers=self.config['header'], params=params)
        return response.data['id']
