from selenium.webdriver.common.by import By



class HeaderMenuLocators:
    HEADER_MENU = (By.CLASS_NAME, "header-menu")
    COMPUTERS_LINK_BUTTON = (By.LINK_TEXT, "Computers")
    NOTEBOOKS_LINK_TEXT = (By.LINK_TEXT, "Notebooks")

class HeaderMenu:

    def __init__(self, driver):
        self.driver = driver
        self.header_menu = self.driver.find_element(*HeaderMenuLocators.HEADER_MENU)

    def hover_over_and_get_sublist(self, element):
        pass

