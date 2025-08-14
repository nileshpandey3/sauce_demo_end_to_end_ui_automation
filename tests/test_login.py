import pytest
from pages.login_page import LoginPage
from setup import BASE_URL, HOMEPAGE_TITLE, STANDARD_PASSWORD, STANDARD_USERNAME

@pytest.mark.login
class TestLogin:

    @classmethod
    def setup_class(cls):
        pass
    
    @pytest.mark.standard_login
    def test_standard_login(self):
        # Perform and verify a standard login
        LoginPage.login(
            url=BASE_URL,
            page_title=HOMEPAGE_TITLE,
            username=STANDARD_USERNAME,
            password=STANDARD_PASSWORD,
            )
        print(self.page.title())
        
        

    @classmethod
    def teardown_class(cls):
        pass