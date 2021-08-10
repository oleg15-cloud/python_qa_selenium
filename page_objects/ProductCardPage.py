from selenium.webdriver.common.by import By


class ProductCardPage:
    MESSAGE_SUCCESS_ADD_TO_THE_CART = "//div[@class='alert alert-success alert-dismissible']"
    BTN_ADD_TO_CART = (By.XPATH, "//button[@id='button-cart']")
    FULL_SCREEN_PICTURE = "//figure/img"
