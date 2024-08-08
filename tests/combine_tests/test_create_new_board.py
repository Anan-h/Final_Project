import logging
import os
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from infra.web.browser_wrapper import BrowserWrapper
from logic.api.api_boards import APIBoards
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from logic.web.opening_page import OpeningPage


class TestCreateNewBoard(unittest.TestCase):
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
        self.api_boards = APIBoards(self.api_request)

    def tearDown(self):
        board_id = self.response.data['id']
        self.home_page.log_out()
        self.api_boards.delete_board_by_id(board_id)
        self.driver.quit()

    def test_create_new_board(self):
        logging.info('Testing the creating new board function')
        self.home_page = HomePage(self.driver)
        board_name = Utils.generate_random_string(5)
        self.response = self.api_boards.create_new_board(board_name)
        boards_names = self.home_page.get_boards_names()
        self.assertTrue(self.home_page.board_is_visible())
        self.assertIn(board_name, boards_names)
