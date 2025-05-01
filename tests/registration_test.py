from common.base_test import BaseTest
from helpers.DataGenerator import DataGenerator
from test_data.csv_helper import CsvDataManager

class RegistrationTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.registration_page = self.home_page.header.click_register_button()

    def test_successful_registration_all_fields(self):
        data_generator = DataGenerator()
        correct_email = data_generator.generate_valid_email()
        correct_password = data_generator.generate_valid_password()
        self.registration_page.select_random_gender()
        self.registration_page.enter_first_name(data_generator.generate_valid_firstName())
        self.registration_page.enter_last_name(data_generator.generate_valid_lastName())
        self.registration_page.enter_email(correct_email)
        self.registration_page.enter_company_name(data_generator.generate_random_company_name())
        self.registration_page.enter_main_password(correct_password)
        self.registration_page.enter_confirm_password(correct_password)
        registration_result_page = self.registration_page.click_register_button()

        self.assertEqual("Your registration completed", registration_result_page.get_register_result_message())

        CsvDataManager.save_credentials_in_csv_file("../test_data/valid_login_credentials", correct_email, correct_password)






