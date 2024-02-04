
class WelcomePageLocators(object):
   LOGIN_BUTTON = "a.Buttonsstyles__Button-sc-1jwidxo-0:nth-child(1)"
class LoginPageLocators(object):
   EMAIL_INPUT = "#username"
   PASSWORD_INPUT = "#password"
   LOGIN_BUTTON = "#login-submit"
   ERROR_MESSAGE = "#username-uid2-error"
   LOGIN_BUTTON_ATTLASIAN = "#login-submit"


class BoardsPageLocators(object):
   USER_ICON = '.js-open-header-member-menu'
   BOARDS_SECTION = ".all-boards"
   LOGOUT_BUTTON = 'div:nth-child(5) > ul:nth-child(3) > li:nth-child(1) > button:nth-child(1) > span'
   LOGOUT_BUTTON_ATTLASIAN = "#logout-submit"


class AfterLogoutPageLocators(object):
   LOGIN_REGISTER_BUTTONS = "a.global-header-section-button.mod-primary"