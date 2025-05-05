import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from helpers.support_functions import wait_5s_until_element_is_visible


class PasswordRecoveryPageLocators:
    EMAIL_INPUT = (By.ID, "Email")
    EMAIL_FIELD_ERROR = (By.ID, "Email-error")
    BAR_NOTIFICATION = (By.CSS_SELECTOR, ".bar-notification")
    BAR_NOTIFICATION_CONTENT = (By.CSS_SELECTOR, "p.content")
    RECOVER_BUTTON = (By.CSS_SELECTOR, ".password-recovery-button")

class PasswordRecoveryPage(BasePage):

    @allure.step
    def enter_email(self, email):
        el = self.driver.find_element(*PasswordRecoveryPageLocators.EMAIL_INPUT)
        el.send_keys(email)
        el.send_keys(Keys.TAB)

    @allure.step
    def get_email_field_validation_error(self):
        el = self.driver.find_element(*PasswordRecoveryPageLocators.EMAIL_FIELD_ERROR)
        return el.text

    @allure.step
    def is_notification_bar_displayed(self):
        el = wait_5s_until_element_is_visible(self.driver, PasswordRecoveryPageLocators.BAR_NOTIFICATION)
        return el.is_displayed()

    @allure.step
    def get_notification_bar_content(self):
        el = wait_5s_until_element_is_visible(self.driver, PasswordRecoveryPageLocators.BAR_NOTIFICATION_CONTENT)
        return el.text

    @allure.step
    def click_recover_button(self):
        self.driver.find_element(*PasswordRecoveryPageLocators.RECOVER_BUTTON).click()