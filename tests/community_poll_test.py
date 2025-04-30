# from common.base_test import BaseTest
#
#
# class CommunityPollTest(BaseTest):
#
#     def test_voting_in_community_poll_without_selecting_any_button(self):
#         self.home_page.click_vote_button()
#         self.assertEqual("Please select an answer", self.home_page.get_alert_text())
#
#     # DOES NOT WORK - SAME ISSUE AS NEWSLETTER, JS/COOKIES - TO BE INVESTIGATED
#     def test_only_logged_user_can_vote_in_poll(self):
#         self.home_page.select_random_poll_radio_button()
#         self.home_page.click_vote_button()
#         self.assertEqual("Only registered users can vote."
#                          , self.home_page.get_community_poll_validation_message())