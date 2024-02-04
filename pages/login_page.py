import time
from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from playwright.sync_api import expect


class LoginPage(BasePage):
    
    def __init__(self, browser):
        super().__init__(browser)
    '''
    Method check is page open
    '''
    def is_opened(self):
        expect(self.page.locator(LoginPageLocators.LOGIN_BUTTON)).to_be_visible()

    '''
    Method for login in.
    '''
    def login(self, user, expected_error=False):
        self.fill_fields(user,expected_error)
        self.click(self.element(LoginPageLocators.LOGIN_BUTTON))

    '''
    Method for filling in fields
    '''
    def fill_fields(self, user, expected_error):
        self.type(self.element(LoginPageLocators.EMAIL_INPUT), user._email)
        self.click(self.element(LoginPageLocators.LOGIN_BUTTON))
        if expected_error is True:
            return
        self.type(self.element(LoginPageLocators.PASSWORD_INPUT), user._password)
    


# The commented code is a method called `is_error_message()` in the `LoginPage` class. This method
# checks if an error message is displayed on the login page.
    '''
    Method checks if error message is displayed
    '''
    def is_error_message(self): 
        expect(self.page.locator(LoginPageLocators.ERROR_MESSAGE)).to_be_visible()
     
    '''
    Method checks if the login is failed
    '''
    def is_login_failed(self):
        self.is_opened()
        self.is_error_message()
    