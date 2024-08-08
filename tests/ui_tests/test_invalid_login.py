import logging
import os
import unittest
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from infra.web.browser_wrapper import BrowserWrapper
from logic.web.login_page import LoginPage
from logic.web.opening_page import OpeningPage


class TestInvalidLogin(unittest.TestCase):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, '../../config.json')
    config = ConfigProvider().load_from_file(config_path)

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["base_url"])
        self.first_page = OpeningPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_invalid_log_in(self):
        """
        Test Case- 7
        performing login process with invalid password
        """
        logging.info('Testing tha login function with invalid password')
        self.first_page.login_button_click()
        login_page = LoginPage(self.driver)
        login_page.fill_email_input(self.config['email'])
        login_page.click_on_continue_button()
        login_page.fill_password_input(Utils.generate_random_string(5))
        login_page.click_on_continue_button()
        self.assertTrue(login_page.error_message_is_visible())
