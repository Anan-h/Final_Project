from infra.logger import Logger


class BasePage:

    def __init__(self, driver):
        self._driver = driver

    def refresh(self):
        self._driver.refresh()
