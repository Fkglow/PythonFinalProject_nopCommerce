from selenium.webdriver.common.by import By

from pages.contact_us_page import ContactUsPage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.top_menu_links import TopMenuLInks


class HeaderMenuLocators:
    HEADER_MENU = (By.CLASS_NAME, "header-menu")
    HEADER_MENU_LINKS = (By.CSS_SELECTOR, "ul.top-menu")

class HeaderMenu:

    def __init__(self, driver):
        self.driver = driver
        self.header_menu = self.driver.find_element(*HeaderMenuLocators.HEADER_MENU)

    def get_top_menu_links_list(self):
        links = self.driver.find_elements(*HeaderMenuLocators.HEADER_MENU_LINKS)
        return links

    def select_link_from_top_menu_by_text(self, category_name):
        el = self.driver.find_element(By.LINK_TEXT, category_name)
        el.click()
        match category_name:
            case TopMenuLInks.SEARCH.value:
                return SearchPage(self.driver)
            case TopMenuLInks.MY_ACC.value:
                return LoginPage(self.driver)
            case TopMenuLInks.CONTACT.value:
                return ContactUsPage(self.driver)
            case _:
                print("Category_name does not match any page")



