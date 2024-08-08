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


class TestDeleteBoard(unittest.TestCase):
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

    def tearDown(self):
        self.home_page.log_out()

    def test_deleting_board_function(self):
        self.home_page.click_on_board()
        self.board = BoardPage(self.driver)
        self.board.click_on_board_menu()
        self.board.click_on_close_button()
        self.board.confirm_closing_board()
        self.board.click_on_delete_board_button()
        self.board.click_on_confirm_delete_board_button()
        self.assertTrue(self.board.board_deleted_message_is_visible())



