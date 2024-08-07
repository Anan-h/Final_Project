from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from infra.web.base_page import BasePage


class OpeningPage(BasePage):
    LOGIN_BUTTON = "//a[contains(text(),'Log in')]"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
        except NoSuchElementException as e:
            print(e)

    def login_button_click(self):
        """ Clicks on the login button. """
        self._login_button.click()