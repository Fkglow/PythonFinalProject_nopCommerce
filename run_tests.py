import unittest
# from tests.community_poll_test import CommunityPollTest
from tests.newsletter_test import NewsletterTest
from tests.registration_test import RegistrationTest

# community_poll_tests = unittest.TestLoader().loadTestsFromTestCase(CommunityPollTest)
newsletter_tests = unittest.TestLoader().loadTestsFromTestCase(NewsletterTest)
registration_tests = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)

tests_for_run = [
    newsletter_tests,
    registration_tests
]

test_suite = unittest.TestSuite(tests_for_run)

unittest.TextTestRunner().run(test_suite)