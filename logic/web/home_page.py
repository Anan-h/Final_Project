import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from logic.web.app_base_page import AppBasePage


class HomePage(AppBasePage):
    BOARD_NAME = "//div[@class='LinesEllipsis  '] "
    NEW_BOARD = "//a[@class='board-tile']"

    def __init__(self, driver):
        super().__init__(driver)

    def board_is_visible(self):
        """
        a function that checks if the board is displayed on the screen
        :return: True/False
        """
        try:
            board = WebDriverWait(self._driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.NEW_BOARD)))
            return board.is_displayed()
        except TimeoutException as e:
            logging.error(f'an error occurred: {e}')

    def get_boards_names(self):
        """
        a function that extracts the names of the boards
        :return: all the names as list
        """
        try:
            board_names = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_all_elements_located((By.XPATH, self.BOARD_NAME)))
            board_names_text = []
            for i in range(len(board_names)):
                board_names_text.append(board_names[i].text)
            return board_names_text
        except TimeoutException as e:
            logging.error(f'an error occurred: {e}')

    def click_on_board(self):
        try:
            board = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.NEW_BOARD)))
            board.click()
        except TimeoutException as e:
            logging.error(f'an error occurred: {e}')
