from selenium.webdriver.common.by import By

from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators, BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

