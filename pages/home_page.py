import random

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from components.footer import Footer
from components.header import Header
from components.header_menu import HeaderMenu
from helpers.support_functions import wait_5s_until_element_is_visible


class HomePageLocators:
    COOKIE_BANNER = (By.ID, "eu-cookie-bar-notification")
    COOKIE_BANNER_CLOSE_BUTTON = (By.ID, "eu-cookie-ok")
    # COMMUNITY POLL
    COMMUNITY_POLL_RADIO_BUTTONS = (By.CSS_SELECTOR, ".answer input")
    VOTE_BUTTON = (By.ID, "vote-poll-1")
    COMMUNITY_POLL_VALIDATION_MESSAGE = (By.ID, "block-poll-vote-error-1")

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(self.driver)
        self.header_menu = HeaderMenu(self.driver)
        self.footer = Footer(self.driver)
        self.close_cookie_banner()

    @allure.step
    def close_cookie_banner(self):
        try:
            cookie_banner = self.driver.find_element(*HomePageLocators.COOKIE_BANNER)
            cookie_close_button = self.driver.find_element(*HomePageLocators.COOKIE_BANNER_CLOSE_BUTTON)
            if cookie_banner.is_displayed():
                cookie_close_button.click()
        except NoSuchElementException:
            pass

    @allure.step
    def get_community_poll_radio_buttons_list(self):
        return self.driver.find_elements(*HomePageLocators.COMMUNITY_POLL_RADIO_BUTTONS)

    @allure.step
    def select_random_poll_radio_button(self):
        random_nr = random.randint(0,3)
        radios = self.get_community_poll_radio_buttons_list()
        radios[random_nr].click()

    @allure.step
    def click_vote_button(self):
        self.driver.find_element(*HomePageLocators.VOTE_BUTTON).click()

    @allure.step
    def get_alert_text(self):
        alert = self.wait_5s.until(EC.alert_is_present())
        return alert.text

    @allure.step
    def get_community_poll_validation_message(self):
        el = wait_5s_until_element_is_visible(self.driver, HomePageLocators.COMMUNITY_POLL_VALIDATION_MESSAGE)
        return el.text

