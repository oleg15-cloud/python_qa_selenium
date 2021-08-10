from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from page_objects.AdminLoginPage import AdminLoginPage


def test_check_error_message(browser, url):
    browser.get(f"{url}/admin/")
    browser.find_element(*AdminLoginPage.BTN_LOGIN).click()
    WebDriverWait(browser, 1).until(ec.visibility_of_element_located((By.XPATH, AdminLoginPage.ERROR_MESSAGE)))
