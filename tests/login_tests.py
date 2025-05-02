import random

from ddt import data, unpack, ddt
from tests.base_test import BaseTest
from helpers.DataGenerator import DataGenerator
from helpers.csv_helper import CsvDataManager

@ddt
class LoginTests(BaseTest):

    def setUp(self):
        super().setUp()
        self.login_page = self.home_page.header.click_login_button()

    @data(*CsvDataManager.get_credentials_from_csv_file("../test_data/valid_login_credentials"))
    @unpack
    def test_successful_login(self, email, password):
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_log_in_button()
        self.assertEqual("Log out", self.home_page.header.get_login_button_text())

    def test_incorrect_password_validation(self):
        random_valid_email = random.choice(CsvDataManager.get_emails_from_csv_file("../test_data/valid_login_credentials"))
        self.login_page.enter_email(random_valid_email)
        self.login_page.enter_password(DataGenerator().generate_valid_password())
        self.login_page.click_log_in_button()
        error_message = self.login_page.get_login_summary_validation_error_message().replace('\n', ' ')
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect"
                         , error_message)

    def test_login_as_non_existing_user(self):
        self.login_page.enter_email(DataGenerator().generate_valid_email())
        self.login_page.enter_password(DataGenerator().generate_valid_password())
        self.login_page.click_log_in_button()
        self.assertTrue(self.login_page.is_validation_message_displayed())
        error_message = self.login_page.get_login_summary_validation_error_message().replace('\n', ' ')
        self.assertEqual("Login was unsuccessful. Please correct the errors and try again. No customer account found"
                         , error_message)

