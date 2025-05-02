from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from helpers.support_functions import *

class BasePage:
    """
    Base class for each page
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait_5s = WebDriverWait(self.driver, timeout=5)
        self.alert = Alert(self.driver)
        self._verify_page()

    def _verify_page(self):
        image_slider = (By.CSS_SELECTOR, ".slider-img")
        wait_5s_until_element_is_visible(self.driver, image_slider)
