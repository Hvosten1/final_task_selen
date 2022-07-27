from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "[id = login_form]")
    REGISTER_FORM = (By.CSS_SELECTOR, "[id = register_form]")


class ProductPageLocators:
    PRODUCT_IMG = (By.CSS_SELECTOR, "[id = product_gallery")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "div.col-sm-6.product_main [type = submit]")
    NAME_OF_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PURCHASE_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    BUCKET_TOTAL = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info strong ")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")