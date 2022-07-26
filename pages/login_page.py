from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators

from selenium import webdriver

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "It's not login page"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "It's no login form on current page"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "It's no register form on current page "
        assert True

    def register_new_user(self, email, password):
        email_element = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password1_element = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password2_element = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        registerButton_element = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_element.send_keys(email)
        password1_element.send_keys(password)
        password2_element.send_keys(password)
        registerButton_element.click()
