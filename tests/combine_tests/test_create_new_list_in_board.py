import logging
import os
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
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, '../../config.json')
    config = ConfigProvider().load_from_file(config_path)

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
        self.board_page.log_out()
        self.api_boards.delete_board_by_id(self.board_id)
        self.driver.quit()

    def test_create_new_list(self):
        logging.info('Testing the creating new list function')
        self.board_page = BoardPage(self.driver)
        self.board_page.click_on_add_new_list_button()
        list_name = Utils.generate_random_string(5)
        self.board_page.fill_in_name_for_new_list(list_name)
        self.board_page.click_on_add_list_button()
        lists_names = self.board_page.get_all_lists_names()
        self.assertIn(list_name, lists_names)


