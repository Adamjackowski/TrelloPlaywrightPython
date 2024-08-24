import inspect
import os
from datetime import datetime
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
    yield browser
    browser.close()

'''
Method for taking the screenshot and saving in the /screenshots directory. It is called in browser fixture
'''
def take_screenshot(browsers, test_name):
    screenshots_dir = parentdir + '\screenshots'
    now = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    screenshot_file_path = '{}\{}_{}.png'.format(screenshots_dir, test_name, now)
    browsers.save_screenshot(screenshot_file_path)
    return screenshot_file_path

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

def screenshot(browsers, request):
    failed_before = request.session.testsfailed
    yield None
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(browsers, test_name)

@pytest.fixture()
def users():
    def _users(user):
        return user
    return _users


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        browser = item.funcargs['browsers']
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # if pytest_html != None:
            #     extra.append(pytest_html.extras.image("file:///" + take_screenshot(browser, item.name)))
            # else:
            #     take_screenshot(browser, item.name)
            None
        report.extra = extra