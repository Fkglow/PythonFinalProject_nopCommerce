from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from helpers.support_functions import wait_5s_until_element_is_visible


class SearchPageLocators:
    SEARCH_INPUT = (By.CLASS_NAME, "search-text")
    ADVANCED_SEARCH_CHECKBOX = (By.ID, "advs")
    SEARCH_IN_DESCRIPTION_CHECKBOX = (By.ID, "sid")
    SEARCH_IN_TAGS_CHECKBOX = (By.ID, "sit")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-button")
    VALIDATION_MESSAGE = (By.CSS_SELECTOR, ".warning")
    RESULT_MESSAGE = (By.CSS_SELECTOR, ".no-result")

class SearchPage(BasePage):

    def click_search_button(self):
        el = self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON)
        el.click()

    def mark_advanced_search_checkbox(self):
        el = self.driver.find_element(*SearchPageLocators.ADVANCED_SEARCH_CHECKBOX)
        el.click()

    def is_search_in_description_checkbox_displayed(self):
        el = wait_5s_until_element_is_visible(self.driver, SearchPageLocators.SEARCH_IN_DESCRIPTION_CHECKBOX)
        return el.is_displayed()

    def is_search_in_tags_checkbox_displayed(self):
        el = wait_5s_until_element_is_visible(self.driver, SearchPageLocators.SEARCH_IN_TAGS_CHECKBOX)
        return el.is_displayed()

    def get_validation_message(self):
        el = wait_5s_until_element_is_visible(self.driver, SearchPageLocators.VALIDATION_MESSAGE)
        return el.text

    def get_search_result_message(self):
        el = wait_5s_until_element_is_visible(self.driver, SearchPageLocators.RESULT_MESSAGE)
        return el.text
