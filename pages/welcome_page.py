import time
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import *
import time
from playwright.sync_api import expect

class WelcomePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.page.goto('https://trello.com')

    '''
    Method for login
    '''
    def login(self):
        self.click(self.element(WelcomePageLocators.LOGIN_BUTTON))
        with self.page.expect_request("https://id.atlassian.com/gateway/api/gasv3/api/v1/batch") as request:
            print(f"{request.value.method} {request.value.url} Request found!")
    '''
    Method  for re open the page
    '''
    def open(self):
        self.page.goto('https://trello.com/pl')
            
    '''
    Method check is page open
    '''
    def is_opened(self):
        # search by css selector
        expect(self.page.locator(WelcomePageLocators.LOGIN_BUTTON)).to_be_visible()
        
        # search by role
        elements  = self.page.get_by_role("img", name="Atlassian Trello").nth(0)
        expect(elements).to_be_visible()
        
        # search by label
        expect(self.page.get_by_label("Atlassian Trello")).to_be_visible
        
        # search by placeholder
        expect(self.page.get_by_placeholder("E-mail address")).to_be_visible
      