import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from infra.web.browser_wrapper import BrowserWrapper
from logic.api.api_boards import APIBoards
from logic.api.api_cards import APICards
from logic.web.board_page import BoardPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from logic.web.opening_page import OpeningPage


class TestMoveCard(unittest.TestCase):
    config = ConfigProvider().load_from_file('../config.json')

    def setUp(self):
        self.api_request = APIWrapper()
        self.driver = BrowserWrapper().get_driver(self.config["base_url"])
        first_page = OpeningPage(self.driver)
        first_page.login_button_click()
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.config["password"])
        self.home_page = HomePage(self.driver)
        self.api_boards = APIBoards(self.api_request)
        self.response = self.api_boards.create_new_board(Utils.generate_random_string(5))
        self.board_id = self.response.data['id']
        self.to_do_list_id = self.api_boards.get_to_do_list_id_by_board_id(self.board_id)

    def tearDown(self):
        self.api_boards.delete_board_by_id(self.board_id)
        self.board_page.log_out()

    def test_move_card_to_done_list(self):
        self.home_page.click_on_board()
        APICards(self.api_request).create_new_card_on_list(self.to_do_list_id, Utils.generate_random_string(5))
        self.board_page = BoardPage(self.driver)
        self.board_page.move_card_to_list(self.config['done_list_name'])
        self.assertTrue(self.board_page.check_that_card_is_in_list(self.config['done_list_name']))
