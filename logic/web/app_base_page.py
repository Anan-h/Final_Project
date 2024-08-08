import logging

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.web.base_page import BasePage


class AppBasePage(BasePage):
    AVATAR = "//div[@data-testid='header-member-menu-avatar']"
    LOGOUT_BTN = "//span[contains(text(),'Log out')]"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self.avatar = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.AVATAR)))
        except TimeoutException as e:
            logging.error(f'an error occurred: {e}')

    def click_on_avatar_icon(self):
        self.avatar.click()

    def click_on_logout_button(self):
        try:
            log_out = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGOUT_BTN)))
            log_out.click()
        except TimeoutException as e:
            logging.error(f'an error occurred: {e}')

    def log_out(self):
        """
        a function to execute the whole process of logging out
        """
        self.click_on_avatar_icon()
        self.click_on_logout_button()

    def avatar_icon_is_visible(self):
        """
        a function that checks if the avatar icon is displayed
        :return: True/False
        """
        return self.avatar.is_displayed()
