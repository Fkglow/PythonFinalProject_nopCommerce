import unittest

from tests.contact_us_form_test import ContactUsFormTest
from tests.login_tests import LoginTests
# from tests.community_poll_test import CommunityPollTest
from tests.newsletter_test import NewsletterTest
from tests.password_recovery_test import PasswordRecoveryTest
from tests.registration_form_validations_test import RegistrationFormValidationTest
from tests.registration_test import RegistrationTest
from tests.search_store_test import SearchStoreTest

# community_poll_tests = unittest.TestLoader().loadTestsFromTestCase(CommunityPollTest)
newsletter_tests = unittest.TestLoader().loadTestsFromTestCase(NewsletterTest)
registration_tests = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)
registration_form_validation_tests = unittest.TestLoader().loadTestsFromTestCase(RegistrationFormValidationTest)
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
contact_us_tests = unittest.TestLoader().loadTestsFromTestCase(ContactUsFormTest)
password_recovery_tests = unittest.TestLoader().loadTestsFromTestCase(PasswordRecoveryTest)
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchStoreTest)


tests_for_run = [
    newsletter_tests,
    registration_tests,
    registration_form_validation_tests,
    login_tests,
    contact_us_tests,
    password_recovery_tests,
    search_tests
]

test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)