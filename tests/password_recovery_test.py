import random

from tests.base_test import BaseTest
from helpers.DataGenerator import DataGenerator
from helpers.csv_helper import CsvDataManager


class PasswordRecoveryTest(BaseTest):

    def setUp(self):
        super().setUp()
        login_page = self.home_page.header.click_login_button()
        self.recover_pass_page = login_page.click_forgot_password()

    def test_recover_password_for_invalid_email(self):
        self.recover_pass_page.enter_email(DataGenerator().generate_valid_email())
        self.recover_pass_page.click_recover_button()
        self.assertTrue(self.recover_pass_page.is_notification_bar_displayed())
        self.assertEqual("Email not found."
                         ,self.recover_pass_page.get_notification_bar_content())

    def test_recover_password_for_valid_email(self):
        random_valid_email = random.choice(CsvDataManager.get_emails_from_csv_file("../test_data/valid_login_credentials"))
        self.recover_pass_page.enter_email(random_valid_email)
        self.recover_pass_page.click_recover_button()
        self.assertTrue(self.recover_pass_page.is_notification_bar_displayed())
        self.assertEqual("Email with instructions has been sent to you."
                         , self.recover_pass_page.get_notification_bar_content())
