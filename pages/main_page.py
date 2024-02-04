import time
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators
import time


class WelcomePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.page.goto("https://trello.com")

    # '''
    # Method for logging out
    # For some reason sometimes the alert window is displayed. Then we logout with this window
    # '''

    # def logout(self):
        
    #     self.close_all_dialogs()
        
    #     self.click(self.element(MainPageLocators.USER_ICON))
        
    #     self.click(self.element(MainPageLocators.LOGOUT_BTN))
    #     try:
    #         WebbrowserWait(self.browser, 1).until(EC.alert_is_present())
    #         alert = self.browser.switch_to.alert
    #         alert.accept()
    #     except TimeoutException:
    #         return self.element(*LoginPageLocators.LOGIN_BTN)
    #     except UnexpectedAlertPresentException:
    #         return False
    #     return self.element(*LoginPageLocators.LOGIN_BTN)

    # '''
    # Method for checking if the page is opened.
    # Method waits for page loads
    # '''

    # def is_opened(self, page):
    #     WebbrowserWait(self.browser, 1).until(EC.invisibility_of_element(
    #             (By.CSS_SELECTOR, "spinner-wrap.ng-scope.show-spinner")))
    #     if page == "ASSISTANCES":
    #         try:
    #              WebbrowserWait(self.browser, 1).until(
    #                 EC.visibility_of_element_located(AssistancesListLocatorsSP.CREATE_ASSISTANCE))
    #         except:
    #             return False
    #         return self.element(*AssistancesListLocatorsSP.CREATE_ASSISTANCE).is_displayed()
    #     if page == "SMARTBOARD":
    #         WebbrowserWait(self.browser, 1).until(
    #             EC.visibility_of_element_located((By.CSS_SELECTOR, "img.photo-icon")))
    #         return self.element(*SmartBoardPageLocators.PLANNED_INTERVENTION_WIDGET).is_displayed()
    #     if page == "TECHNICIANS":
    #         WebbrowserWait(self.browser, 1).until(EC.visibility_of_element_located(
    #             (By.XPATH, "//*[@translate='createTechnician']")))
    #         return self.element(*TechniciansListLocatorsCommon.CREATE_TECHNICIAN).is_displayed()
    #     if page == "USERS":
    #         WebbrowserWait(self.browser, 1).until(EC.visibility_of_element_located(
    #             (By.XPATH, "//*[@translate='createUser']")))
    #         WebbrowserWait(self.browser, 3).until(EC.visibility_of_element_located(UsersListLocatorsCommon.CREATE_USER))
    #         return self.element(*UsersListLocatorsCommon.CREATE_USER).is_displayed() 

    # '''
    # Method for opening the page.
    # For some reason the exception can be called, so there is a try block to handle it
    # '''

    # def open(self, page):
    #     if page == "ASSISTANCES":
    #         try:
    #             self.click(self.element(*MainPageLocators.ASSISTANCES))
    #         except:
    #             WebbrowserWait(self.browser, 1).until(
    #                 EC.invisibility_of_element_located((By.CLASS_NAME, "modal fade ng-isolate-scope ng-animate ng-leave ng-leave-active")))
    #             self.click(self.element(*MainPageLocators.SMART_MANAGER))
    #             self.click(self.element(*MainPageLocators.ASSISTANCES))
    #     if page == "SMARTBOARD":
    #         try:
    #             self.click(self.element(*MainPageLocators.SMART_BOARD))
    #         except:
    #             WebbrowserWait(self.browser, 1).until(
    #                 EC.invisibility_of_element_located((By.CLASS_NAME, "modal fade ng-isolate-scope ng-animate ng-leave ng-leave-active")))
    #             self.click(self.element(*MainPageLocators.SMART_PARTNER))
    #             self.click(self.element(*MainPageLocators.SMART_BOARD))
    #     if page == "TECHNICIANS":
    #         try:
    #             self.click(self.element(*MainPageLocators.TECHNICIANS))
    #         except:
    #             WebbrowserWait(self.browser, 1).until(
    #                 EC.invisibility_of_element_located((By.CLASS_NAME, "modal fade ng-isolate-scope ng-animate ng-leave ng-leave-active")))
    #             self.click(self.element(*MainPageLocators.SMART_MANAGER))
    #             self.click(self.element(*MainPageLocators.TECHNICIANS))
    #     if page == "USERS":
    #         try:
    #             self.click(self.element(*MainPageLocators.USERS))
    #         except:
    #             WebbrowserWait(self.browser, 1).until(
    #                 EC.invisibility_of_element_located((By.CLASS_NAME, "modal fade ng-isolate-scope ng-animate ng-leave ng-leave-active")))
    #             self.click(self.element(*MainPageLocators.SMART_MANAGER))
    #             self.click(self.element(*MainPageLocators.USERS))
    #     return self.is_opened(page)
    # '''
    # Method for refreshing the page.
    # '''

    # def refresh(self):
    #     self.browser.refresh()
    #     return True
