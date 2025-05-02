from tests.base_test import BaseTest
from helpers.DataGenerator import DataGenerator
from pages.top_menu_links import TopMenuLInks


class ContactUsFormTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.contact_us_page = self.home_page.header_menu.select_link_from_top_menu_by_text(TopMenuLInks.CONTACT.value)

    def test_all_input_fields_are_required(self):
        self.contact_us_page.click_submit_button()
        self.assertEqual("Enter your name", self.contact_us_page.get_name_field_validation_error())
        self.assertEqual("Enter email", self.contact_us_page.get_email_field_validation_error())
        self.assertEqual("Enter enquiry", self.contact_us_page.get_enquiry_field_validation_error())

    def test_it_is_possible_to_submit_enquiry(self):
        self.contact_us_page.enter_name(DataGenerator().name())
        self.contact_us_page.enter_email(DataGenerator().generate_valid_email())
        self.contact_us_page.enter_enquiry(DataGenerator().text(max_nb_chars=100))
        self.contact_us_page.click_submit_button()
        self.assertEqual("Your enquiry has been successfully sent to the store owner."
                         ,self.contact_us_page.get_submit_enquiry_result_message())
