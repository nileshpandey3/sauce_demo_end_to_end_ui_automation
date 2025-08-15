import pytest
from playwright.sync_api import expect
from element_selectors.login_selectors import LOGIN_ERROR
from setup import BASE_URL, STANDARD_PASSWORD, STANDARD_USERNAME

@pytest.mark.login
class TestLogin:

    @pytest.mark.standard_login
    def test_standard_login(self, login_page):
        # Perform and verify a standard login
        login_page.load(url=BASE_URL)
        login_page.login(
            username=STANDARD_USERNAME,
            password=STANDARD_PASSWORD,
            )
        title = '' # TODO
    
    @pytest.mark.locked_user
    def test_locked_out_user(self, login_page):
        # Perform and verify login for a locked out user
        login_page.load(url=BASE_URL)
        login_page.login(
            username='locked_out_user',
            password=STANDARD_PASSWORD,
            )
        error = login_page.get_error(locator=LOGIN_ERROR)
        assert 'Epic sadface: Sorry, this user has been locked out.' in error.inner_text()

    @pytest.mark.empty_username
    def test_empty_username(self, login_page):
        login_page.load(url=BASE_URL)
        login_page.login(
            username='',
            password=STANDARD_PASSWORD,
            )
        error = login_page.get_error(locator=LOGIN_ERROR)
        assert 'Username is required' in error.inner_text()
        

    @pytest.mark.empty_password
    def test_empty_username(self, login_page):
        login_page.load(url=BASE_URL)
        login_page.login(
            username=STANDARD_USERNAME,
            password='',
            )
        error = login_page.get_error(locator=LOGIN_ERROR)
        assert 'Password is required' in error.inner_text()