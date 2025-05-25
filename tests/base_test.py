import os
import unittest
from selenium import webdriver
from pages.home_page import HomePage
from helpers.csv_helper import CsvDataManager

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "..", "config", "config.json")
        config = CsvDataManager.load_config(file_path)

        env = os.getenv("ENV", "test")
        url = config["environments"].get(env)
        # Browser can be set via env var, if not first one from config file will be selected
        browser = os.getenv("BROWSER", config["browsers"][0]).lower()
        if not url:
            raise ValueError(f"URL for provided env: {env} cannot be found")

        match browser:
            case "chrome":
                self.driver = webdriver.Chrome()
            case "firefox":
                self.driver = webdriver.Firefox()
            case _:
                raise ValueError(f"Unsupported browser: {browser}")

        self.driver.maximize_window()
        self.driver.get(url)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()