from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from page_objects.ProductCardPage import ProductCardPage


def test_check_message_about_adding_product_to_the_cart(browser, url):
    browser.get(f"{url}/iphone")
    browser.find_element(*ProductCardPage.BTN_ADD_TO_CART).click()
    WebDriverWait(browser, 1).until(
        ec.visibility_of_element_located((By.XPATH, ProductCardPage.MESSAGE_SUCCESS_ADD_TO_THE_CART)))
