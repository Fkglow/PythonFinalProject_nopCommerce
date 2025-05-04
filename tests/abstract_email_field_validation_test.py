from abc import ABC, abstractmethod
from helpers.DataGenerator import DataGenerator
from tests.base_test import BaseTest


class AbstractEmailFieldValidationTest(ABC, BaseTest):

    @abstractmethod
    def get_page(self):
        pass

    def test_invalid_email_validation(self):
        page = self.get_page()
        invalid_email = DataGenerator().generate_invalid_email()
        page.enter_email(invalid_email)
        validation_error = page.get_email_field_validation_error()
        self.assertEqual("Please enter a valid email address.", validation_error)

    def test_email_not_matching_regex_validation(self):
        page = self.get_page()
        wrong_email = DataGenerator().generate_email_that_fails_regex()
        page.enter_email(wrong_email)
        validation_error = page.get_email_field_validation_error()
        self.assertEqual("Wrong email", validation_error)



