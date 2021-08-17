from selenium.webdriver.common.by import By


class MainPage:
    BANNER_IPHONE_6 = \
        "//div[@class='swiper-slide text-center swiper-slide-duplicate swiper-slide-active']/a/img[@alt='iPhone 6']"
    BANNER_MACBOOKAIR = "//div[@class='swiper-slide text-center swiper-slide-active']/img[@alt='MacBookAir']"
    DROPDOWN_MENU_DESKTOPS = (By.XPATH, "//a[text()='Desktops']")
    INPUT_SEARCH = (By.XPATH, "//input[@name='search']")
    BTN_SEARCH = (By.XPATH, "//span[@class='input-group-btn']/button")
