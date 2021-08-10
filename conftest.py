import pytest

from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(options=options)
    elif _browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
    elif _browser == "opera":
        options = OperaOptions()
        if headless:
            options.headless = True
        driver = webdriver.Opera(options=options)

    if maximized:
        driver.maximize_window()

    request.addfinalizer(driver.quit)

    return driver
