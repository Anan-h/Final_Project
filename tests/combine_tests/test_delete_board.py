import logging
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
    config = ConfigProvider().load_from_file('../../config.json', __file__)

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
        self.driver.quit()

    def test_deleting_board_function(self):
        """
        Test Case- 14
        deleting an existent board
        """
        logging.info('Testing the deleting function of a board')
        self.home_page.click_on_board()
        self.board_page = BoardPage(self.driver)
        self.board_page.click_on_board_menu()
        self.board_page.click_on_close_button()
        self.board_page.confirm_closing_board()
        self.board_page.click_on_delete_board_button()
        self.board_page.click_on_confirm_delete_board_button()
        self.assertTrue(self.board_page.board_deleted_message_is_visible())



