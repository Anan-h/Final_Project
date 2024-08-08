import logging
import os
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.api.api_boards import APIBoards
from logic.api.api_cards import APICards
from logic.api.api_lists import APILists


class TestMoveAllCards(unittest.TestCase):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, '../../config.json')
    config = ConfigProvider().load_from_file(config_path)

    def setUp(self):
        self.api_request = APIWrapper()
        self.api_boards = APIBoards(self.api_request)
        self.create_response = self.api_boards.create_new_board(Utils.generate_random_string(5))
        self.board_id = self.create_response.data['id']
        self.to_do_list_id = self.api_boards.get_to_do_list_id_by_board_id(self.board_id)
        self.done_list_id = self.api_boards.get_done_list_id_by_board_id(self.board_id)

    def tearDown(self):
        self.api_boards.delete_board_by_id(self.board_id)

    def test_move_all_cards_from_todo_to_done_list(self):
        logging.info('Testing tha API request for moving all the cards from the all cards')
        self.api_lists = APILists(self.api_request)
        APICards(self.api_request).create_new_card_on_list(self.to_do_list_id, Utils.generate_random_string(5))
        cards_ids = self.api_lists.get_cards_ids_from_list_by_id(self.to_do_list_id)
        move_response = self.api_lists.move_all_cards_from_list_to_list(
            self.to_do_list_id, self.done_list_id, self.board_id)
        cards_ids_in_done_list = self.api_lists.get_cards_ids_from_list_by_id(self.done_list_id)
        self.assertEqual(move_response.status, self.config['good_status_code'])
        self.assertEqual(cards_ids, cards_ids_in_done_list)
