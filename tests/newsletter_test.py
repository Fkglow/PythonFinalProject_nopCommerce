from tests.base_test import BaseTest

class NewsletterTest(BaseTest):

    def test_email_is_required_for_newsletter(self):
        footer = self.home_page.footer
        footer.click_subscribe_button()
        footer.wait_for_subscribe_loader_to_disappear()
        self.assertEqual("Enter valid email", footer.get_newsletter_result_message())

    def test_it_is_possible_to_subscribe_newsletter(self):
        footer = self.home_page.footer
        footer.enter_email_to_newsletter_input("mail@mail.com")
        footer.click_subscribe_button()
        self.assertEqual("Thank you for signing up! A verification email has been sent. We appreciate your interest.", footer.get_newsletter_result_message())


# NOT WORKING! ISSUE WITH COOKIES AND JS
