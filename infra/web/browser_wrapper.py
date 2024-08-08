import os.path

from infra.config_provider import ConfigProvider
from selenium import webdriver


class BrowserWrapper:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(base_dir, '../../config.json')

    def __init__(self):
        self.driver = None
        self.config = ConfigProvider().load_from_file(self.config_file_path)

    def get_driver(self, url):
        """
               This function load a website according to given url, on specific browser that
               is provided from outer file. and launches it on full screen
               :param url: the website link
               :return: opens the website on the desired browser
               """
        if self.config['browser'] == 'Chrome':
            self.driver = webdriver.Chrome()
        elif self.config['browser'] == 'Edge':
            self.driver = webdriver.Edge()
        elif self.config['browser'] == 'FireFox':
            self.driver = webdriver.Firefox()

        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver

