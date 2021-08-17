from selenium.webdriver.common.by import By


class AdminLoginPage:
    BTN_LOGIN = (By.XPATH, "//button[@class='btn btn-primary']")
    ERROR_MESSAGE = "//div[@class='alert alert-danger alert-dismissible']"
