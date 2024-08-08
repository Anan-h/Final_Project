import logging
import os
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


class TestUpdateCard(unittest.TestCase):
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
        self.home = HomePage(self.driver)
        self.api_boards = APIBoards(self.api_request)
        self.response = self.api_boards.create_new_board(Utils.generate_random_string(5))
        self.board_id = self.response.data['id']
        self.to_do_list_id = self.api_boards.get_to_do_list_id_by_board_id(self.board_id)

    def tearDown(self):
        self.board_page.log_out()
        self.api_boards.delete_board_by_id(self.board_id)
        self.driver.quit()

    def test_update_card_name(self):
        logging.info('Testing updating the card name')
        self.home.click_on_board()
        self.board_page = BoardPage(self.driver)
        APICards(self.api_request).create_new_card_on_list(self.to_do_list_id, Utils.generate_random_string(5))
        self.board_page.click_on_the_pen_icon()
        new_name = Utils.generate_random_string(5)
        self.board_page.update_the_card_name(new_name)
        card_name = self.board_page.get_card_name()
        self.assertEqual(new_name, card_name)
