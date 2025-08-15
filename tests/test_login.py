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
            url=BASE_URL,
            username=STANDARD_USERNAME,
            password=STANDARD_PASSWORD,
            )
        expect(login_page).to_have_title('Swag Labs')
    
    @pytest.mark.locked_user
    def test_locked_out_user(self, login_page):
        # Perform and verify login for a locked out user
        login_page.load(url=BASE_URL)
        login_page.login(
            url=BASE_URL,
            username='locked_out_user',
            password=STANDARD_PASSWORD,
            )
        error = login_page.get_error(locator=LOGIN_ERROR)
        assert 'Epic sadface: Sorry, this user has been locked out.' in error.inner_text()
