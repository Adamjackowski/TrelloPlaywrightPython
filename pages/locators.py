
class WelcomePageLocators(object):
   LOGIN_BUTTON = "a.Buttonsstyles__Button-sc-1jwidxo-0:nth-child(1)"
class LoginPageLocators(object):
   EMAIL_INPUT = "#username"
   PASSWORD_INPUT = "#password"
   LOGIN_BUTTON = "#login-submit"
   ERROR_MESSAGE = "#username-uid2-error"
   LOGIN_BUTTON_ATTLASIAN = "#login-submit"
   DISMISS_2FA = "#mfa-promote-dismiss"


class BoardsPageLocators(object):
   USER_ICON = '.js-open-header-member-menu'
   BOARDS_SECTION = ".all-boards"
   LOGOUT_BUTTON = 'nav.IfckxJ5PbpJuxT:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > button:nth-child(1)'
   LOGOUT_BUTTON_ATTLASIAN = "#logout-submit"


class AfterLogoutPageLocators(object):
   LOGIN_REGISTER_BUTTONS = "a.global-header-section-button.mod-primary"