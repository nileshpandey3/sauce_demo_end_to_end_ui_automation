import pytest
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)
