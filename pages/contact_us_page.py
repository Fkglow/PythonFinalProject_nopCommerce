from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from helpers.support_functions import wait_5s_until_element_is_visible


class ContactUsPageLocators:
    NAME_INPUT = (By.ID, "FullName")
    NAME_FIELD_ERROR = (By.ID, "FullName-error")
    EMAIL_INPUT = (By.ID, "Email")
    EMAIL_FIELD_ERROR = (By.ID, "Email-error")
    ENQUIRY_INPUT = (By.ID, "Enquiry")
    ENQUIRY_FIELD_ERROR = (By.ID, "Enquiry-error")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".contact-us-button")
    ENQUIRY_SUBMIT_RESULT_MESSAGE = (By.CSS_SELECTOR, ".result")

class ContactUsPage(BasePage):

    def enter_name(self, name):
        el = self.driver.find_element(*ContactUsPageLocators.NAME_INPUT)
        el.send_keys(name)

    def get_name_field_validation_error(self):
        el = self.driver.find_element(*ContactUsPageLocators.NAME_FIELD_ERROR)
        return el.text

    def enter_email(self, email):
        el = self.driver.find_element(*ContactUsPageLocators.EMAIL_INPUT)
        el.send_keys(email)

    def get_email_field_validation_error(self):
        el = self.driver.find_element(*ContactUsPageLocators.EMAIL_FIELD_ERROR)
        return el.text

    def enter_enquiry(self, name):
        el = self.driver.find_element(*ContactUsPageLocators.ENQUIRY_INPUT)
        el.send_keys(name)

    def get_enquiry_field_validation_error(self):
        el = self.driver.find_element(*ContactUsPageLocators.ENQUIRY_FIELD_ERROR)
        return el.text

    def click_submit_button(self):
        el = self.driver.find_element(*ContactUsPageLocators.SUBMIT_BUTTON)
        el.click()

    def get_submit_enquiry_result_message(self):
        el = wait_5s_until_element_is_visible(self.driver, ContactUsPageLocators.ENQUIRY_SUBMIT_RESULT_MESSAGE)
        return el.text



