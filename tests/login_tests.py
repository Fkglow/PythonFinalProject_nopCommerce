from ddt import data, unpack, ddt
from common.base_test import BaseTest
from helpers.DataGenerator import DataGenerator
from test_data.csv_helper import CsvDataManager

@ddt
class LoginTests(BaseTest):

    def setUp(self):
        super().setUp()
        self.login_page = self.home_page.header.click_login_button()

    def test_login_with_invalid_credentials(self):
        self.login_page.enter_email(DataGenerator().generate_valid_email())
        self.login_page.enter_password(DataGenerator().generate_valid_password())
        self.login_page.click_log_in_button()
        self.assertTrue(self.login_page.is_validation_message_displayed())
        error_message = self.login_page.get_login_summary_validation_error_message().replace('\n', ' ')
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again. No customer account found"
                         , error_message)

    @data(*CsvDataManager.get_credentials_from_csv_file("../test_data/valid_login_credentials"))
    @unpack
    def test_successful_login(self, email, password):
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_log_in_button()
        self.assertEqual("Log out", self.home_page.header.get_login_button_text())
