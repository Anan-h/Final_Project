import logging
import os
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.api.api_boards import APIBoards
from logic.api.api_members import APIMembers
from logic.enums.member_types import MemberTypes


class TestRemoveMemberFromBoard(unittest.TestCase):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, '../../config.json')
    config = ConfigProvider().load_from_file(config_path)

    def setUp(self):
        self.api_request = APIWrapper()
        self.api_boards = APIBoards(self.api_request)
        self.creating_board_response = self.api_boards.create_new_board(Utils.generate_random_string(5))
        self.board_id = self.creating_board_response.data['id']
        self.member_type = Utils.generate_random_value_of_enum(MemberTypes)
        self.member_id = APIMembers(self.api_request).get_member_id_by_user_name(self.config['user_name_to_add'])
        self.api_boards.add_member_to_board(self.board_id, self.member_id, self.member_type)

    def tearDown(self):
        self.api_boards.delete_board_by_id(self.board_id)

    def test_deleting_member_from_board(self):
        """
        Test case- 5
        API Test -deleting member from board by id
        """
        logging.info('Testing tha API request for deleting member from a board')
        delete_response = self.api_boards.remove_member_from_board(self.board_id, self.member_id)
        self.assertEqual(delete_response.status, self.config['good_status_code'])
