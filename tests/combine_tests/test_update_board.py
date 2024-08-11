import logging
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from infra.web.browser_wrapper import BrowserWrapper
from logic.api.api_boards import APIBoards
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from logic.web.opening_page import OpeningPage


class TestUpdateBoard(unittest.TestCase):
    config = ConfigProvider().load_from_file('../../config.json', __file__)

    def setUp(self):
        self.api_request = APIWrapper()
        self.driver = BrowserWrapper().get_driver(self.config["base_url"])
        first_page = OpeningPage(self.driver)
        first_page.login_button_click()
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.config["password"])
        HomePage(self.driver)
        self.api_boards = APIBoards(self.api_request)
        self.response = self.api_boards.create_new_board(Utils.generate_random_string(5))
        self.board_id = self.response.data['id']

    def tearDown(self):
        self.api_boards.delete_board_by_id(self.board_id)
        HomePage(self.driver).log_out()

    def test_update_board_name(self):
        """
        Test Case- 2
        Updating the name of the board
        """
        logging.info('Testing updating the board name')
        new_board_name = Utils.generate_random_string(5)
        self.api_boards.update_board_name_by_board_id(self.board_id, new_board_name)
        HomePage(self.driver).refresh()
        boards_names = HomePage(self.driver).get_boards_names()
        self.assertIn(new_board_name, boards_names)
