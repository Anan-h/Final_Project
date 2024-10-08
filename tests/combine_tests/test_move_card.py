import logging
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.jira_handler import JiraHandler
from infra.utils import Utils
from infra.web.browser_wrapper import BrowserWrapper
from logic.api.api_boards import APIBoards
from logic.api.api_cards import APICards
from logic.web.board_page import BoardPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from logic.web.opening_page import OpeningPage


class TestMoveCard(unittest.TestCase):
    config = ConfigProvider().load_from_file('../../config.json', __file__)

    def tearDown(self):
        if self.error:
            JiraHandler().create_issue(self.config['project_key'], self._testMethodName, self.error)
        self.board_page.log_out()
        self.api_boards.delete_board_by_id(self.board_id)
        self.driver.quit()

    def test_move_card_from_todo_to_done_list(self):
        """
        Test Case- 13
        performing full process to move card from To-Do list to Done list
        """
        logging.info('Testing moving card from ToDo list to the Done list')
        # pre-conditions
        self.error = None
        self.api_request = APIWrapper()
        self.driver = BrowserWrapper().get_driver(self.config["base_url"])
        first_page = OpeningPage(self.driver)
        first_page.login_button_click()
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.config["password"])
        self.home_page = HomePage(self.driver)
        # test steps
        self.api_boards = APIBoards(self.api_request)
        self.response = self.api_boards.create_new_board(Utils.generate_random_string(5))
        self.board_id = self.response.data['id']
        self.home_page.click_on_board()
        self.board_page = BoardPage(self.driver)
        self.to_do_list_id = self.api_boards.get_to_do_list_id_by_board_id(self.board_id)
        self.api_cards = APICards(self.api_request)
        self.api_cards.create_new_card_on_list(self.to_do_list_id, Utils.generate_random_string(5))
        # Act
        self.board_page.move_card_to_list(self.config['done_list_name'])
        # Assert
        try:
            self.assertTrue(self.board_page.check_that_card_is_in_list(self.config['done_list_name']))
            # self.assertTrue(False)  # intentionally to demonstrate jira
        except AssertionError as e:
            self.error = f"An error occurred: {e}"
            raise
