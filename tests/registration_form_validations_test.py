from tests.base_test import BaseTest
from helpers.DataGenerator import DataGenerator


class RegistrationFormValidationTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.registration_page = self.home_page.header.click_register_button()

    def test_required_fields_are_validated(self):
        required_fields = ['First name', 'Last name', 'Email', 'Confirm password']
        self.registration_page.click_register_button()
        self.assertEqual(required_fields, self.registration_page.get_list_of_fields_with_validation_errors())
        self.assertEqual("First name is required.", self.registration_page.get_field_error("First name"))
        self.assertEqual("Last name is required.", self.registration_page.get_field_error("Last name"))
        self.assertEqual("Email is required.", self.registration_page.get_field_error("Email"))
        self.assertEqual("Password is required.", self.registration_page.get_field_error("Confirm password"))

    def test_invalid_email_is_validated(self):
        invalid_email = DataGenerator().generate_invalid_email()
        self.registration_page.enter_email(invalid_email)
        error_message = self.registration_page.get_field_error("Email")
        self.assertEqual("Please enter a valid email address.", error_message)

    def test_email_not_matching_regex_is_validated(self):
        wrong_email = DataGenerator().generate_email_that_fails_regex()
        self.registration_page.enter_email(wrong_email)
        error_message = self.registration_page.get_field_error("Email")
        self.assertEqual("Wrong email", error_message)

    def test_invalid_password_validation(self):
        invalid_password = DataGenerator().generate_invalid_password()
        self.registration_page.enter_main_password(invalid_password)
        error_message = self.registration_page.get_field_error("Password")
        self.assertEqual("Password must meet the following rules: must have at least 6 characters and not greater than 64 characters"
                         ,error_message)

    def test_passwords_must_match(self):
        password = DataGenerator().generate_valid_password()
        self.registration_page.enter_main_password(password)
        self.registration_page.enter_confirm_password(f"{password}TEST")
        error_message = self.registration_page.get_field_error("Confirm password")
        self.assertEqual("The password and confirmation password do not match.", error_message)
