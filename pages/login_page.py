import allure
from selenium.webdriver import Keys

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from helpers.support_functions import wait_5s_until_element_is_visible
from pages.password_recovery_page import PasswordRecoveryPage


class LoginPageLocators:
    REGISTER_BUTTON = (By.CLASS_NAME, "register-button")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")
    EMAIL_INPUT = (By.ID, "Email")
    EMAIL_FIELD_ERROR = (By.ID, "Email-error")
    PASSWORD_INPUT = (By.ID, "Password")
    FORGOT_PASSWORD_LINK_BUTTON = (By.CLASS_NAME, "forgot-password")
    LOGIN_VALIDATION_ERROR = (By.CLASS_NAME, "validation-summary-errors")

class LoginPage(BasePage):

    @allure.step
    def enter_email(self, email):
        el = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        el.send_keys(email)
        el.send_keys(Keys.TAB)

    @allure.step
    def get_email_field_validation_error(self):
        el = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD_ERROR)
        return el.text

    @allure.step
    def enter_password(self, password):
        el = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        el.send_keys(password)
        el.send_keys(Keys.TAB)

    @allure.step
    def click_log_in_button(self):
        el = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        el.click()

    @allure.step
    def click_register_button(self):
        el = self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON)
        el.click()

    @allure.step
    def click_forgot_password(self):
        el = self.driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK_BUTTON)
        el.click()
        return PasswordRecoveryPage()

    @allure.step
    def is_validation_message_displayed(self):
        el = wait_5s_until_element_is_visible(self.driver, LoginPageLocators.LOGIN_VALIDATION_ERROR)
        return el.is_displayed()

    @allure.step
    def get_login_summary_validation_error_message(self):
        el = self.driver.find_element(*LoginPageLocators.LOGIN_VALIDATION_ERROR)
        return el.text

    @allure.step
    def click_forgot_password(self):
        el = self.driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK_BUTTON)
        el.click()
        return PasswordRecoveryPage(self.driver)


