
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def busket_is_empty(self):

        empt = self.browser.find_element(*BasketPageLocators.STATUS)
        text = empt.text
        assert text == " Your basket is empty. "

    def busket_is_not_empty(self):

        empt = self.browser.find_element(*BasketPageLocators.STATUS)
        text = empt.text
        assert text != " Your basket is empty. "