from tests.base_test import BaseTest
from pages.top_menu_links import TopMenuLInks


class SearchStoreTest(BaseTest):

    def test_alert_appears_on_clicking_search_without_product(self):
        self.home_page.header.click_search_button()
        self.assertEqual("Please enter some search keyword", self.home_page.get_alert_text())

    def test_searching_unexisting_product(self):
        self.home_page.header.enter_product_in_search_input("Test")
        search_store_page = self.home_page.header.click_search_button()
        result = search_store_page.get_search_result_message()
        self.assertEqual("No products were found that matched your criteria.", result)

    def test_term_min_length_validation(self):
        self.home_page.header.enter_product_in_search_input("ab")
        search_store_page = self.home_page.header.click_search_button()
        result = search_store_page.get_validation_message()
        self.assertEqual("Search term minimum length is 3 characters", result)

    def test_new_options_are_displayed_after_checking_advanced_search(self):
        search_page = self.home_page.header_menu.select_link_from_top_menu_by_text(TopMenuLInks.SEARCH.value)
        search_page.mark_advanced_search_checkbox()
        self.assertTrue(search_page.is_search_in_description_checkbox_displayed())
        self.assertTrue(search_page.is_search_in_tags_checkbox_displayed())