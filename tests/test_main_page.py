from page_objects.MainPage import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def test_check_visibility_of_iphone_6_banner(browser, url):
    browser.get(url)
    WebDriverWait(browser, 6).until(ec.visibility_of_element_located((By.XPATH, MainPage.BANNER_IPHONE_6)))


def test_check_visibility_of_macbookair_banner(browser, url):
    browser.get(url)
    WebDriverWait(browser, 4).until(ec.visibility_of_element_located((By.XPATH, MainPage.BANNER_MACBOOKAIR)))


def test_check_visibility_of_desktops_dropdown_menu(browser, url):
    browser.get(url)
    browser.find_element(*MainPage.DROPDOWN_MENU_DESKTOPS)


def test_check_visibility_of_search_input(browser, url):
    browser.get(url)
    browser.find_element(*MainPage.INPUT_SEARCH)


def test_check_visibility_of_search_button(browser, url):
    browser.get(url)
    browser.find_element(*MainPage.BTN_SEARCH)
