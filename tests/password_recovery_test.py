import os
import random

import allure

from tests.abstract_email_field_validation_test import AbstractEmailFieldValidationTest
from helpers.DataGenerator import DataGenerator
from helpers.csv_helper import CsvDataManager

@allure.title("Password recovery")
class PasswordRecoveryTest(AbstractEmailFieldValidationTest):

    def setUp(self):
        super().setUp()
        login_page = self.home_page.header.click_login_button()
        self.recover_pass_page = login_page.click_forgot_password()

    @allure.title("Password recovery attempt for an unregistered email")
    def test_recover_password_for_invalid_email(self):
        self.recover_pass_page.enter_email(DataGenerator().generate_valid_email())
        self.recover_pass_page.click_recover_button()
        self.assertTrue(self.recover_pass_page.is_notification_bar_displayed())
        self.assertEqual("Email not found."
                         ,self.recover_pass_page.get_notification_bar_content())

    @allure.title("Password recovery for a valid email")
    def test_recover_password_for_valid_email(self):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "..", "test_data", "valid_login_credentials")
        random_valid_email = random.choice(CsvDataManager.get_emails_from_csv_file(file_path))
        self.recover_pass_page.enter_email(random_valid_email)
        self.recover_pass_page.click_recover_button()
        self.assertTrue(self.recover_pass_page.is_notification_bar_displayed())
        self.assertEqual("Email with instructions has been sent to you."
                         , self.recover_pass_page.get_notification_bar_content())

    @allure.title("Invalid email validation")
    def test_invalid_email_is_validated(self):
        self.invalid_email_validation_test()

    @allure.title("Email not matching regex validation")
    def test_email_not_matching_regex_is_validated(self):
        self.email_not_matching_regex_validation_test()

    def get_page(self):
        return self.recover_pass_page
