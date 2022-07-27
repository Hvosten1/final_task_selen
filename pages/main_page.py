from selenium.webdriver.common.by import By

from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators, BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_bucket(self):
        bucket_elem = WebDriverWait(self.browser, 3).until(
            EC.element_to_be_clickable(BasePageLocators.BUCKET_BUTTON)
            )
        bucket_elem.click()