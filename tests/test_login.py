import os, sys, inspect
import pytest
import time
import json
from pages.objects.user import User
from pages.welcome_page import WelcomePage
from pages.login_page import LoginPage
from pages.boards_page import BoardsPage

class TestLogin():
  @pytest.mark.e2e
  def test_login_success(self, browsers, users):
    # Init necesarry objects
    user = users(User())
    welcome_page = WelcomePage(browsers)
    login_page = LoginPage(browsers)
    boards_page = BoardsPage(browsers)

   # Test steps
    welcome_page.is_opened()
    welcome_page.login()
    login_page.is_opened()
    login_page.login(user)
    boards_page.is_opened()
    boards_page.logout()
    welcome_page.is_opened()
  
  @pytest.mark.xfail(reason="Test is failing, beaasuse of ...")  
  def test_login_success_failing(self, browsers, users):
    # Init necesarry objects
    user = users(User("It_will_fail", "And_we_expect_it"))
    welcome_page = WelcomePage(browsers)
    login_page = LoginPage(browsers)
    boards_page = BoardsPage(browsers)

   # Test steps
    welcome_page.is_opened()
    welcome_page.login()
    login_page.is_opened()
    login_page.login(user)

  @pytest.mark.login_failed
  def test_login_fail(self, browsers, users):
    # Init necesarry objects
    user = users(User("", ""))
    welcome_page = WelcomePage(browsers)
    login_page = LoginPage(browsers)

    # Test steps
    welcome_page.is_opened()
    welcome_page.login()
    login_page.is_opened()
    login_page.login(user, expected_error=True)
    login_page.is_login_failed()
    welcome_page.open()
  
  