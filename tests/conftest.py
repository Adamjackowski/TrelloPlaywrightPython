import inspect
import os
from datetime import datetime
from pathlib import Path
import pytest


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)


def pytest_addoption(parser):
    parser.addoption("--test_browser", action="store", default="Edge")


@pytest.fixture(autouse=True, scope='session')
def declared_browser(pytestconfig):
    return pytestconfig.getoption("test_browser")


'''
Fixture method for init and deinit browser before and after all tests. It is called once a test session.
When test fails, the screenshot is beeing taken
'''
@pytest.fixture(scope='session')
def browsers(playwright, declared_browser):
    choosen_browser = declared_browser
    browser = None
    if choosen_browser == "Chrome":
        browser = playwright.chromium.launch(headless=False)
        browser.new_page()
    elif choosen_browser == "Firefox":
        browser = playwright.firefox.launch(headless=False)
        browser.new_page()
    elif choosen_browser == "Edge":
        browser = playwright.chromium.launch(headless=False, channel="msedge")
        browser.new_page()
    elif choosen_browser == "Safari":
        browser = playwright.webkit.launch(headless=False)
        browser.new_page()
    browser.new_context(locale="en-GB")
    yield browser
    browser.close()

'''
Method for taking the screenshot and saving in the /screenshots directory. It is called in browser fixture
'''
def take_screenshot(browsers, test_name):
    screenshots_dir = Path(f"{parentdir}/screenshots")
    now = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    screenshot_file_name = '{}_{}.png'.format(test_name, now)
    screenshot_file_path = Path(f"{screenshots_dir}/{screenshot_file_name}")
    browsers.contexts[0].pages[0].screenshot(path = screenshot_file_path)
    return screenshot_file_path

@pytest.fixture()
def users():
    def _users(user):
        return user
    return _users


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        browser = item.funcargs['browsers']
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
                extra.append(pytest_html.extras.image(str(take_screenshot(browser, item.name))))
        else:
            None
            #take_screenshot(browser, item.name)  
        report.extra = extra