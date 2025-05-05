import allure

from tests.abstract_email_field_validation_test import AbstractEmailFieldValidationTest
from helpers.DataGenerator import DataGenerator
from pages.top_menu_links_enum import TopMenuLInks

@allure.title("Contact us form")
class ContactUsFormTest(AbstractEmailFieldValidationTest):

    def setUp(self):
        super().setUp()
        self.contact_us_page = self.home_page.header_menu.select_link_from_top_menu_by_text(TopMenuLInks.CONTACT.value)

    @allure.title("Required fields validation")
    def test_all_input_fields_are_required(self):
        self.contact_us_page.click_submit_button()
        self.assertEqual("Enter your name", self.contact_us_page.get_name_field_validation_error())
        self.assertEqual("Enter email", self.contact_us_page.get_email_field_validation_error())
        self.assertEqual("Enter enquiry", self.contact_us_page.get_enquiry_field_validation_error())

    @allure.title("Submitting enquiry")
    def test_it_is_possible_to_submit_enquiry(self):
        self.contact_us_page.enter_name(DataGenerator().name())
        self.contact_us_page.enter_email(DataGenerator().generate_valid_email())
        self.contact_us_page.enter_enquiry(DataGenerator().text(max_nb_chars=100))
        self.contact_us_page.click_submit_button()
        self.assertEqual("Your enquiry has been successfully sent to the store owner."
                         ,self.contact_us_page.get_submit_enquiry_result_message())

    @allure.title("Invalid email validation")
    def test_invalid_email_is_validated(self):
        self.invalid_email_validation_test()

    @allure.title("Email not matching regex validation")
    def test_email_not_matching_regex_is_validated(self):
        self.email_not_matching_regex_validation_test()

    def get_page(self):
        return self.contact_us_page