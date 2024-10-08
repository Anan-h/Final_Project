import logging
import unittest
from infra.config_provider import ConfigProvider
from infra.web.browser_wrapper import BrowserWrapper
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from logic.web.opening_page import OpeningPage


class TestValidLogin(unittest.TestCase):
    config = ConfigProvider().load_from_file('../../config.json', __file__)

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["base_url"])
        self.first_page = OpeningPage(self.driver)

    def tearDown(self):
        HomePage(self.driver).log_out()
        self.driver.quit()

    def test_valid_log_in(self):
        """
        Test Case- 6
        performing login process with valid data
        """
        logging.info('Testing the login function with valid data')
        self.first_page.login_button_click()
        login_page = LoginPage(self.driver)
        login_page.fill_email_input(self.config['email'])
        login_page.click_on_continue_button()
        login_page.fill_password_input(self.config['password'])
        login_page.click_on_continue_button()
        avatar_visible = HomePage(self.driver).avatar_icon_is_visible()
        self.assertTrue(avatar_visible)
