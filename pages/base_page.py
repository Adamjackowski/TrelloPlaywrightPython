from pages.locators import *
from playwright.sync_api import expect


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser
        self.page = browser.contexts[0].pages[0]
    '''
    Method which convert the locator to web element
    '''
    def element(self, locator):
        return self.page.locator(locator)
    
    '''
    Method which input the text to text fields
    '''
    def type(self, element, value):
        return element.fill(value)
        
    '''
    Method clicks on the element
    '''
    def click(self, element):
        return element.click()

    
    '''
    Method which gets the placeholder value of text field
    '''
    def get_input_value(self, element):
        return element.get_attribute("value")
    