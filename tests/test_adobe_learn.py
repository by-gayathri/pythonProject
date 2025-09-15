import time

import pytest
from playwright.sync_api import Page, expect
from pages.learn_page import LearnPage


class TestAdobeLearnPage:
    """Tests for https://www.adobe.com/learn"""

    def test_page_loads_successfully(self, learn_page: LearnPage) -> None:
        """Page should return HTTP 200 and fully load."""
        url = learn_page.page.url
        assert url == "https://www.adobe.com/learn"

    def test_title_contains_adobe(self, learn_page: LearnPage) -> None:
        """Page title should include the word 'Adobe'."""
        title = learn_page.page.title()
        assert title == "Adobe Learn"
    
    def test_title_not_contains_adobe(self, learn_page: LearnPage) -> None:
            """Page title should not include the word 'Adobe'."""
            title = learn_page.page.title()
            assert title != "Adobe iLearn"

    def test_learn_photoshop(self, learn_page: LearnPage) -> None:
        """Learn Adobe photoshop should work"""
        learn_page.locator('data-testid=product-nav-card-photoshop').click()
        learn_page.wait_for_visible('data-test-id=learn-topics-button-all', timeout=15_000)
        time.sleep(15)
        url = learn_page.page.url
        assert url == "https://www.adobe.com/learn"
        # learn_page.locator('data-testid=learn-topics-button-generative-ai').click()
        # # learn_page.locator('span:has-text("Generative AI")').click(timeout=15_000)
        # learn_page.locator('li span:has-text("Beginner"):visible').click()
        #
        # # click on first course
        # learn_page.locator("div[data-test-id^='tutorial-card']").first.click()
