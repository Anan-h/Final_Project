from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def close_browser(self):
        self._driver.close()

    def refresh_browser(self):
        self._driver.refresh()
