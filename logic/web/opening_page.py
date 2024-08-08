import logging
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.web.base_page import BasePage


class OpeningPage(BasePage):
    LOGIN_BUTTON = '//a[@class="Buttonsstyles__Button-sc-1jwidxo-0 kTwZBr"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self.login_button = WebDriverWait(self._driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGIN_BUTTON)))
        except TimeoutException as e:
            logging.error(f'an error occurred: {e}')

    def login_button_click(self):
        """ Clicks on the login button. """
        self.login_button.click()
