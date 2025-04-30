from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.wishlist_page import WishListPage


class HeaderLocators:
    # UPPER HEADER
    CURRENCY_SELECT = (By.ID, "customerCurrency")
    HEADER_LINKS = (By.CLASS_NAME, "header-links")
    REGISTER_LINK_BUTTON = (By.CLASS_NAME, "ico-register")
    LOG_IN_LINK_BUTTON = (By.CLASS_NAME, "ico-login")
    WISHLIST_LINK_BUTTON = (By.CLASS_NAME, "ico-wishlist")
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
    def get_selected_currency(self):
        return self.currency_select.all_selected_options

    def select_currency_by_visible_text(self, currency):
        self.currency_select.select_by_visible_text(currency)

    def click_register_button(self):
        self.header_links.find_element(*HeaderLocators.REGISTER_LINK_BUTTON).click()
        return RegistrationPage(self.driver)

    def click_login_button(self):
        self.header_links.find_element(*HeaderLocators.LOG_IN_LINK_BUTTON).click()
        return LoginPage(self.driver)

    def click_wishlist_button(self):
        self.header_links.find_element(*HeaderLocators.WISHLIST_LINK_BUTTON).click()
        return WishListPage(self.driver)

    def get_wishlist_count(self):
        el = self.driver.find_element(By.CSS_SELECTOR, "span.wishlist-qty")
        el_text =  el.getText()
        wishlist_count = int(el_text.strip("()"))
        return wishlist_count

    def get_shopping_cart_count(self):
        el = self.driver.find_element(By.CSS_SELECTOR, "span.cart-qty")
        el_text =  el.getText()
        shopping_cart_count = int(el_text.strip("()"))
        return shopping_cart_count

    # LOWER HEADER
    def search_product(self, product_name):
        self.driver.find_element(*HeaderLocators.SEARCH_INPUT).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(*HeaderLocators.SEARCH_BUTTON).click()