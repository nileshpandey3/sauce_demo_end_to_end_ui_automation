from playwright.sync_api import Page, expect
from element_selectors.login_selectors import HAMBURGER_MENU, LOGOUT_SIDEBAR_LINK, TITLE, USERNAME, PASSWORD, LOGIN_BTN
from setup import BASE_URL, HOMEPAGE_URL

class LoginPage:

    def __init__(self, page:Page):
        self.page = page
    
    def load(self, url:str):
        self.page.goto(url=url)
        return self.page

    def username_input(self, username):
        return self.page.locator(USERNAME).fill(username)
    
    def passowrd_input(self, password):
        return self.page.locator(PASSWORD).fill(password)
    
    def get_error(self, locator):
        return self.page.locator(locator)
    
    def logout(self):
        if self.page.url == HOMEPAGE_URL:
            self.page.get_by_role("button", name=HAMBURGER_MENU).click()
            self.page.locator(LOGOUT_SIDEBAR_LINK)
            assert self.page.url == BASE_URL

    def login(self, username:str, password:str):
        # login using the supplied credentials
        self.username_input(username)
        self.passowrd_input(password)
        self.page.locator(selector=LOGIN_BTN).click()
        return self.page