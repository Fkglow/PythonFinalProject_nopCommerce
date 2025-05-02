from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.search_page import SearchPage
from helpers.support_functions import *


class HeaderLocators:
    # UPPER HEADER
    CURRENCY_SELECT = (By.ID, "customerCurrency")
    HEADER_LINKS = (By.CLASS_NAME, "header-links")
    REGISTER_LINK_BUTTON = (By.CLASS_NAME, "ico-register")
    LOG_IN_LINK_BUTTON = (By.CSS_SELECTOR, ".header-links ul li:nth-child(2) a")
    SHOPPING_CART_LINK_BUTTON = (By.ID, "topcartlink")
    # LOWER HEADER
    SEARCH_INPUT = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-box-button")

class Header:

    def __init__(self, driver):
        self.driver = driver
        self.header_links = self.driver.find_element(*HeaderLocators.HEADER_LINKS)
        # VERSION WITH CURRENCY SELECT
        # self.currency_select = Select(self.driver.find_element(*HeaderLocators.CURRENCY_SELECT))

    # UPPER HEADER
    # def get_selected_currency(self):
    #     return self.currency_select.all_selected_options
    #
    # def select_currency_by_visible_text(self, currency):
    #     self.currency_select.select_by_visible_text(currency)

    def click_register_button(self):
        self.header_links.find_element(*HeaderLocators.REGISTER_LINK_BUTTON).click()
        return RegistrationPage(self.driver)

    def click_login_button(self):
        self.header_links.find_element(*HeaderLocators.LOG_IN_LINK_BUTTON).click()
        return LoginPage(self.driver)

    def get_login_button_text(self):
        el = wait_5s_until_element_is_visible(self.driver, HeaderLocators.LOG_IN_LINK_BUTTON)
        return el.text

    def get_shopping_cart_count(self):
        el = self.driver.find_element(By.CSS_SELECTOR, "span.cart-qty")
        el_text =  el.getText()
        shopping_cart_count = int(el_text.strip("()"))
        return shopping_cart_count

    # LOWER HEADER
    def enter_product_in_search_input(self, product_name):
        self.driver.find_element(*HeaderLocators.SEARCH_INPUT).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(*HeaderLocators.SEARCH_BUTTON).click()
        return SearchPage(self.driver)