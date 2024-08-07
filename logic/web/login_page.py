from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.web.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_EMAIL_INPUT = '//input[@type="email"]'
    LOGIN_PASSWORD_INPUT = '//input[@type="password"]'
    CONTINUE_BUTTON = '//button[@id="login-submit"]'
    LOGIN_ERROR = '//section[@data-testid="form-error"]'

    def __init__(self, driver):
        super().__init__(driver)

    def fill_email_input(self, email):
        """ Fills the login email input with the given email. """

        try:
            login_email_input = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGIN_EMAIL_INPUT)))
            login_email_input.send_keys(email)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def fill_password_input(self, password):
        """ Fills the login password input with the given password. """

        try:
            login_password_input = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGIN_PASSWORD_INPUT)))
            login_password_input.send_keys(password)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def click_on_continue_button(self):
        try:
            continue_button = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CONTINUE_BUTTON)))
            continue_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def login_flow(self, email, password):
        """
        Executes the login flow with the given email and password.
        :param email: the email address
        :param password: the password
        """
        self.fill_email_input(email)
        self.click_on_continue_button()
        self.fill_password_input(password)
        self.click_on_continue_button()

    def error_message_is_visible(self):
        """
        a function that checks if the invalid loging error message is displayed
        :return: True/False
        """
        try:
            error_msg = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.LOGIN_ERROR)))
            return error_msg.is_displayed()
        except NoSuchElementException as e:
            print(e)
