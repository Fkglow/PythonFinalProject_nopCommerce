import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from helpers.support_functions import wait_5s_until_element_is_visible
from pages.registration_result_page import RegistrationResultPage


class RegistrationPageLocators:
    FIELD_VALIDATION_ERROR = (By.CSS_SELECTOR, "span[class$='-error'] span")
    # PERSONAL DETAILS
    GENDER_RADIO_BUTTONS = (By.CSS_SELECTOR, ".gender input")
    FIRST_NAME_INPUT = (By.ID, "FirstName")
    LAST_NAME_INPUT = (By.ID, "LastName")
    EMAIL_INPUT = (By.ID, "Email")
    # COMPANY DETAILS
    COMPANY_NAME_INPUT = (By.ID, "Company")
    # OPTIONS
    NEWSLETTER_CHECKBOX = (By.ID, "Newsletter")
    # PASSWORD SECTION
    PASSWORD_INPUT = (By.ID, "Password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "ConfirmPassword")

    REGISTER_BUTTON = (By.ID, "register-button")

class RegistrationPage(BasePage):

    def select_random_gender(self):
        random_nr = random.randint(0,1)
        radio_buttons = self.driver.find_elements(*RegistrationPageLocators.GENDER_RADIO_BUTTONS)
        radio_buttons[random_nr].click()

    def enter_first_name(self, firstName):
        el = self.driver.find_element(*RegistrationPageLocators.FIRST_NAME_INPUT)
        el.send_keys(firstName)

    def enter_last_name(self, lastName):
        el = self.driver.find_element(*RegistrationPageLocators.LAST_NAME_INPUT)
        el.send_keys(lastName)

    def enter_email(self, email):
        el = self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        el.clear()
        el.send_keys(email)
        el.send_keys(Keys.TAB)      #required to reload field validation

    def enter_company_name(self, name):
        el = self.driver.find_element(*RegistrationPageLocators.COMPANY_NAME_INPUT)
        el.send_keys(name)

    def enter_main_password(self, password):
        el = self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        el.send_keys(password)
        el.send_keys(Keys.TAB)  # required to reload field validation

    def enter_confirm_password(self, password):
        el = self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT)
        el.send_keys(password)
        el.send_keys(Keys.TAB)  # required to reload field validation

    def click_register_button(self):
        self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        validation_errors = self.driver.find_elements(By.CLASS_NAME, "field-validation-error")
        if validation_errors:
            return RegistrationPage(self.driver)
        else:
            return RegistrationResultPage(self.driver)

    def get_list_of_fields_with_validation_errors(self):
        error_field_labels = []
        validation_errors = self.driver.find_elements(*RegistrationPageLocators.FIELD_VALIDATION_ERROR)
        for error in validation_errors:
            id = str(error.get_attribute('id'))
            id_sep = id.split('-')
            label = self.driver.find_element(By.CSS_SELECTOR, f"[for={id_sep[0]}")
            error_field_labels.append(label.text.rstrip(':'))
        return error_field_labels

    def get_field_error(self, field_name):
        input = self.driver.find_element(By.XPATH, f"//label[contains(text(), '{field_name}')]")
        input_id = input.get_attribute("for")
        try:
            error_mess_locator = (By.CSS_SELECTOR, f"#{input_id}-error")
            error_message = wait_5s_until_element_is_visible(self.driver, error_mess_locator)
            return error_message.text
        except TimeoutException:
            print("Element was not found")
            return None

