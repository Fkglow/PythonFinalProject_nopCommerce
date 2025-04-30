from selenium.webdriver.common.by import By

from common.base_page import BasePage
from helpers.support_functions import *
from selenium.webdriver.support import expected_conditions as EC


class FooterLocators:
   # NEWSLETTER
   NEWSLETTER_EMAIL_INPUT = (By.ID, "newsletter-email")
   SUBSCRIBE_BUTTON = (By.ID, "newsletter-subscribe-button")
   NEWSLETTER_VALIDATION_MESSAGE = (By.ID, "newsletter-result-block")
   SUBSCRIBE_LOADER = (By.ID, "subscribe-loading-progress")

class Footer(BasePage):

    def enter_email_to_newsletter_input(self, email):
        el = self.driver.find_element(*FooterLocators.NEWSLETTER_EMAIL_INPUT)
        scroll_into_view(self.driver, el)
        el.send_keys(email)

    def click_subscribe_button(self):
        el = self.driver.find_element(*FooterLocators.SUBSCRIBE_BUTTON)
        scroll_into_view(self.driver, el)
        el.click()

    def wait_for_subscribe_loader_to_disappear(self):
        self.wait_5s.until(EC.invisibility_of_element_located(FooterLocators.SUBSCRIBE_LOADER))

    def get_newsletter_result_message(self):
        el = self.wait_5s.until(EC.visibility_of_element_located(FooterLocators.NEWSLETTER_VALIDATION_MESSAGE))
        return el.text


