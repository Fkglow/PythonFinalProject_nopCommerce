from common.base_test import BaseTest
from helpers.DataGenerator import DataGenerator
from pages.registration_result_page import RegistrationResultPage
from test_data.csv_helper import CsvDataManager

class RegistrationTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.registration_page = self.home_page.header.click_register_button()

    def test_successful_registration_all_fields(self):
        data_generator = DataGenerator()
        correct_email = data_generator.generate_correct_email()
        correct_password = data_generator.generate_valid_password()
        self.registration_page.select_random_gender()
        self.registration_page.enter_first_name(data_generator.generate_correct_firstName())
        self.registration_page.enter_last_name(data_generator.generate_correct_lastName())
        self.registration_page.enter_email(correct_email)
        self.registration_page.enter_company_name(data_generator.generate_random_company_name())
        self.registration_page.enter_main_password(correct_password)
        self.registration_page.enter_confirm_password(correct_password)
        registration_result_page = self.registration_page.click_register_button()

        self.assertEqual("Your registration completed", registration_result_page.get_register_result_message())

        CsvDataManager.save_credentials_in_csv_file("../test_data/valid_login_credentials", correct_email, correct_password)

    def test_required_fields_are_validated(self):
        required_fields = ['First name', 'Last name', 'Email', 'Confirm password']
        self.registration_page.click_register_button()
        self.assertEqual(required_fields, self.registration_page.get_list_of_fields_with_validation_errors())
        for field in required_fields:
            self.assertEqual(f"{field} is required.",self.registration_page.get_field_error(field))
#             TODO: This should be improved, or deleted as Confirm password field is not ok







