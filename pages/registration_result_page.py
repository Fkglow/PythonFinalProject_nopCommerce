from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from helpers.support_functions import wait_5s_until_element_is_visible


class RegistrationResultPageLocators:
    PAGE_BODY = (By.CSS_SELECTOR, ".registration-result-page")
    CONTINUE_LINK_BUTTON = (By.CSS_SELECTOR, ".register-continue-button")
    RESULT_MESSAGE = (By.CSS_SELECTOR, ".result")

class RegistrationResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_to_load()

    def wait_for_page_to_load(self):
        wait_5s_until_element_is_visible(self.driver, RegistrationResultPageLocators.PAGE_BODY)

    def click_continue_button(self):
        self.driver.find_element(*RegistrationResultPageLocators.CONTINUE_LINK_BUTTON).click()

    def get_register_result_message(self):
        el = self.driver.find_element(*RegistrationResultPageLocators.RESULT_MESSAGE)
        return el.text
