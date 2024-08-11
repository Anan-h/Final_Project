import logging
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from infra.web.browser_wrapper import BrowserWrapper
from logic.api.api_boards import APIBoards
from logic.api.api_members import APIMembers
from logic.enums.member_types import MemberTypes
from logic.web.board_page import BoardPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from logic.web.opening_page import OpeningPage


class AddMemberToBoard(unittest.TestCase):
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
        self.member_type = Utils.generate_random_value_of_enum(MemberTypes)
        self.member_id = APIMembers(self.api_request).get_member_id_by_user_name(self.config['user_name_to_add'])

    def tearDown(self):
        self.board_page.log_out()
        self.api_boards.delete_board_by_id(self.board_id)
        self.driver.quit()

    def test_add_member_to_board(self):
        """
        Test Case- 4
        adding member to board
        """
        logging.info('Testing adding a member to an existent board')
        self.api_boards.add_member_to_board(self.board_id, self.member_id, self.member_type)
        self.home_page.click_on_board()
        self.board_page = BoardPage(self.driver)
        board_members_count = self.board_page.get_how_many_members_in_board()
        self.assertGreater(board_members_count, self.config['min_members_count'])
