import logging
import os
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.api.api_boards import APIBoards


class TestDeletingBoard(unittest.TestCase):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, '../../config.json')
    config = ConfigProvider().load_from_file(config_path)

    def setUp(self):
        self.api_request = APIWrapper()
        self.api_boards = APIBoards(self.api_request)
        self.response = self.api_boards.create_new_board(Utils.generate_random_string(5))
        self.board_id = self.response.data['id']

    def test_update_board_name(self):
        logging.info('Testing tha API request for deleting an existent board')
        delete_response = self.api_boards.delete_board_by_id(self.board_id)
        self.assertEqual(delete_response.status, self.config['good_status_code'])
