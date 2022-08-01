from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #BUCKET_BUTTON = (By.CSS_SELECTOR,"#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs "
                                    # "> span > a")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "[id = login_form]")
    REGISTER_FORM = (By.CSS_SELECTOR, "[id = register_form]")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name = registration-email]")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "[name = registration-password1]")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "[name = registration-password2]")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name = registration_submit]")


class ProductPageLocators:
    PRODUCT_IMG = (By.CSS_SELECTOR, "[id = product_gallery]")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "div.col-sm-6.product_main [type = submit]")
    NAME_OF_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PURCHASE_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    BUCKET_TOTAL = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info strong ")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    #BUCKET_BUTTON =(By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")

class BasketPageLocators:
    STATUS = (By.CSS_SELECTOR, "div [id=content_inner] p")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUCKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")