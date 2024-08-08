import time

from logic.web.app_base_page import AppBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains


class BoardPage(AppBasePage):
    SHARE_BUTTON = "//span[contains(text(),'Share')]"
    USER_NAME_INPUT = "//input[@data-testid='add-members-input']"
    INVITE_OPTION = "//div[@class='member-container']"
    SUBMIT_SHARE_BTN = "//button[@data-testid='team-invite-submit-button']"
    BOARD_MEMBERS = "//button[@data-testid='board-facepile-member']"
    CARD = "//div[@data-testid='trello-card']"
    PEN_ICON = "//button[@data-testid='quick-card-editor-button']"
    CARD_EDIT_TEXT_AREA = "//textarea[@data-testid='quick-card-editor-card-title']"
    SAVE_BUTTON = "//button[@type='submit']"
    CARD_NAME = "//a[@data-testid='card-name']"
    ADD_LIST_BTN = "//button[@data-testid='list-composer-button']"
    NEW_LIST_NAME = "//textarea[@name='Enter list name…']"
    ADD_LIST_SUBMIT_BTN = "//button[@data-testid='list-composer-add-list-button']"
    LISTS_NAMES = "//div[@data-testid='list-header']//h2"
    MENU_BUTTON = "//button[@aria-label='Show menu']"
    CLOSE_BOARD_BTN = "//a[@class='board-menu-navigation-item-link board-menu-navigation-item-link-v2 js-close-board']"
    CONFIRM_CLOSE = "//input[@data-testid='close-board-confirm-button']"
    CLOSE_MSG = "//div[@id='content-wrapper']//div[@class='js-react-root']//div/p"
    DELETE_BTN = "//button[@data-testid='close-board-delete-board-button']"
    CONFIRM_DELETE = "//button[@data-testid='close-board-delete-board-confirm-button']"
    DELETE_MSG = "//div[@id='FlagGroup']//span"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self.share_button = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.SHARE_BUTTON)))

        except NoSuchElementException as e:
            print(e)

    def get_how_many_members_in_board(self):
        """
        a function that checks how many members are in the board
        :return: the amount of the members
        """
        board_members = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_any_elements_located((By.XPATH, self.BOARD_MEMBERS)))

        return len(board_members)

    def click_on_share_button(self):
        self.share_button.click()

    def card_is_visible(self):
        """
        a function that checks if the card is displayed
        :return: True/False
        """
        try:
            card = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CARD)))
            return card.is_displayed()
        except NoSuchElementException as e:
            print(e)

    def click_on_the_pen_icon(self):
        try:
            card = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CARD)))
            ActionChains(self._driver).move_to_element(card).perform()
            pen = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.PEN_ICON)))
            pen.click()
        except NoSuchElementException as e:
            print(e)

    def click_on_save_button(self):
        try:
            save_btn = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.SAVE_BUTTON)))
            save_btn.click()
        except NoSuchElementException as e:
            print(e)

    def update_the_card_name(self, new_name):
        """
        a function that updates the name of the card
        :param new_name: the name to change for
        """
        try:
            text_area = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CARD_EDIT_TEXT_AREA)))
            text_area.clear()
            text_area.send_keys(new_name)
            self.click_on_save_button()
        except NoSuchElementException as e:
            print(e)

    def get_card_name(self):
        try:
            card_name = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CARD_NAME)))
            return card_name.text
        except NoSuchElementException as e:
            print(e)

    def click_on_add_new_list_button(self):
        try:
            add_btn = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.ADD_LIST_BTN)))
            add_btn.click()
        except NoSuchElementException as e:
            print(e)

    def fill_in_name_for_new_list(self, name):
        try:
            text_area = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.NEW_LIST_NAME)))
            text_area.clear()
            text_area.send_keys(name)
        except NoSuchElementException as e:
            print(e)

    def click_on_add_list_button(self):
        try:
            submit_btn = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.ADD_LIST_SUBMIT_BTN)))
            submit_btn.click()
        except NoSuchElementException as e:
            print(e)

    def get_all_lists_names(self):
        try:
            names = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_all_elements_located((By.XPATH, self.LISTS_NAMES)))
            names_texts = []
            for i in range(len(names)):
                names_texts.append(names[i].text)
            return names_texts
        except NoSuchElementException as e:
            print(e)

    def click_on_board_menu(self):
        try:
            menu = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.MENU_BUTTON)))
            menu.click()
        except NoSuchElementException as e:
            print(e)

    def click_on_close_button(self):
        try:
            close_button = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CLOSE_BOARD_BTN)))
            close_button.click()
        except NoSuchElementException as e:
            print(e)

    def confirm_closing_board(self):
        try:
            confirm_button = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CONFIRM_CLOSE)))
            confirm_button.click()
        except NoSuchElementException as e:
            print(e)

    def closing_message_is_displayed(self):
        try:
            msg = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CLOSE_MSG)))
            return msg.is_displayed()
        except NoSuchElementException as e:
            print(e)

    def check_that_card_is_in_list(self, list_name):
        """
        a function that checks if the card is in certain list
        :param list_name: the name of the list
        :return: True/False
        """
        card_locator = f"//li[.//div/h2[text()='{list_name}']]//ol//li//div//div//a[@data-testid='card-name']"
        try:
            card = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, card_locator)))
            return card.is_displayed()
        except NoSuchElementException as e:
            print(f"the card is not in the {list_name} list ")

    def move_card_to_list(self, list_name):
        """
        a function that move a card to certain list by dragging it and dropping in the desired list
        :param list_name: the name of the list to move for
        """
        list_locator = f"//li[.//div/h2[text()='{list_name}']]"
        try:
            card = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CARD_NAME)))
            desired_list = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, list_locator)))

            action = ActionChains(self._driver)
            action.drag_and_drop(card, desired_list).perform()
        except NoSuchElementException as e:
            print(e)

    def click_on_delete_board_button(self):
        """
        a function that clicks on the permanently delete board button
        """
        try:
            delete_button = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.DELETE_BTN)))
            delete_button.click()
        except NoSuchElementException as e:
            print(e)

    def click_on_confirm_delete_board_button(self):
        """
        a function that clicks on the confirm delete red button
        """
        try:
            confirm_delete_btn = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.CONFIRM_DELETE)))
            confirm_delete_btn.click()
        except NoSuchElementException as e:
            print(e)

    def board_deleted_message_is_visible(self):
        """
        a function that checks if the board deleted message is displayed
        :return True/False
        """
        try:
            delete_msg = WebDriverWait(self._driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.DELETE_MSG)))
            return delete_msg.is_displayed()
        except NoSuchElementException as e:
            print(e)
