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

    '''
    Method  for re open the page
    '''
    def open(self):
        self.page.goto('https://trello.com')
            
    '''
    Method check is page open
    '''
    def is_opened(self):
        expect(self.page.locator(WelcomePageLocators.LOGIN_BUTTON)).to_be_visible()