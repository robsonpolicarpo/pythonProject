import pytest
from selene.support.shared import browser
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pytest_html_reporter import attach

URL_BASE = ''


@pytest.fixture(scope='function')
def web():
    yield


def pytest_sessionstart(session):
    setup_browser(URL_BASE, get_options().headless)


def pytest_sessionfinish(session, exitstatus):
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call':
        xfail = hasattr(rep, 'wasxfail')
        if (rep.skipped and xfail) or (rep.failed and not xfail):
            try:
                if 'web' in item.fixturenames:
                    attach(data=browser.config.driver.get_screenshot_as_png())
            except Exception as e:
                print(f'Exception while screenshot browser \n{e}')


def get_options():
    return pytest.__pytestPDB._config.option


def pytest_addoption(parser):
    parser.addoption('--env',
                     default='local',
                     action='store',
                     help='local or remote')
    parser.addoption('--headless',
                     default='false',
                     action='store',
                     help='Headless')


def setup_browser(url, headless):
    if headless in ['true', 'True', True]:
        browser.config.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=chrome_options({'headless': True}))
    if get_options().env == 'remote':
        browser.set_driver(webdriver.Remote(
            command_executor='http://localhost:4444',
            desired_capabilities={'browserName': 'chrome'}
        ))
    browser.config.browser_name = 'chrome'
    browser.config.base_url = url
    browser.config.timeout = 7


def chrome_options(opt):
    options = webdriver.ChromeOptions()
    options.headless = opt['headless']
    # options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    return options
