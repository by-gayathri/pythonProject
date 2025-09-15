import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://www.adobe.com/learn"


@pytest.fixture
def learn_page(page: Page, base_url: str):
    """Navigate to Adobe Learn and return the page object."""
    from pages.learn_page import LearnPage
    lp = LearnPage(page)
    lp.navigate(base_url)
    return lp