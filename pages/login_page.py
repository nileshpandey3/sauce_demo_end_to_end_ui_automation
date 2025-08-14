from playwright.sync_api import Page, expect

class LoginPage:

    def __init__(self, page:Page):
        self.page = page

    def login(self, username:str, password:str):
        # login using the supplied credentials
        self.page.locator(selector='').click()
        self.page.locator(selector='').click()
        self.page.locator(selector='').click()