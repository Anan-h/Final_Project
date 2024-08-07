import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from infra.web.browser_wrapper import BrowserWrapper
from logic.api.api_boards import APIBoards
from logic.web.board_page import BoardPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from logic.web.opening_page import OpeningPage


class TestCreateNewListInBoard(unittest.TestCase):
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
        self.home_page.click_on_board()

    def tearDown(self):
        self.api_boards.delete_board_by_id(self.board_id)
        self.home_page.log_out()

    def test_create_new_list(self):
        board = BoardPage(self.driver)
        board.click_on_add_new_list_button()
        list_name = Utils.generate_random_string(5)
        board.fill_in_name_for_new_list(list_name)
        board.click_on_add_list_button()
        lists_names = board.get_all_lists_names()
        self.assertIn(list_name, lists_names)


