from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
#
# from components.footer import Footer
# from components.header import Header
# from components.header_menu import HeaderMenu


class BasePage:
    """
    Base class for each page
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait_5s = WebDriverWait(self.driver, timeout=5)
        self.alert = Alert(self.driver)
        self._verify_page()
        #
        # self.header = Header(self.driver)
        # self.header_menu = HeaderMenu(self.driver)
        # self.footer = Footer(self.driver)

    def _verify_page(self):
    # TODO:
        return