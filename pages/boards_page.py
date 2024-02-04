import time
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import *
from pages.base_page import *
import time


class BoardsPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    '''
    Method check is page open
    '''
    def is_opened(self):
        expect(self.page.locator(BoardsPageLocators.BOARDS_SECTION)).to_be_visible()


    '''
    Method for logout
    '''
    def logout(self):      
        self.click(self.element(BoardsPageLocators.USER_ICON))
        self.click(self.element(BoardsPageLocators.LOGOUT_BUTTON))
        self.click(self.element(BoardsPageLocators.LOGOUT_BUTTON_ATTLASIAN))
        
 