from playwright.sync_api import Page, expect
from element_selectors.login_selectors import USERNAME, PASSWORD, LOGIN_BTN

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


    def login(self, username:str, password:str):
        # login using the supplied credentials
        self.username_input(username)
        self.passowrd_input(password)
        self.page.locator(selector=LOGIN_BTN).click()
        return self.page