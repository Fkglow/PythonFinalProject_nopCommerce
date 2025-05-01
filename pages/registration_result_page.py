from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from common.base_page import BasePage

class RegistrationResultPageLocators:
    PAGE_BODY = (By.CSS_SELECTOR, ".registration-result-page")
    CONTINUE_LINK_BUTTON = (By.CSS_SELECTOR, ".register-continue-button")
    RESULT_MESSAGE = (By.CSS_SELECTOR, ".result")

class RegistrationResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_to_load()

    def wait_for_page_to_load(self):
        self.wait_5s.until(EC.presence_of_element_located(RegistrationResultPageLocators.PAGE_BODY))

    def click_continue_button(self):
        self.driver.find_element(*RegistrationResultPageLocators.CONTINUE_LINK_BUTTON).click()

    def get_register_result_message(self):
        el = self.driver.find_element(*RegistrationResultPageLocators.RESULT_MESSAGE)
        return el.text
