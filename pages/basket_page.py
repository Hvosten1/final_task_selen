
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def busket_is_empty(self):

        assert self.is_element_present(*BasketPageLocators.STATUS)

    def busket_is_not_empty(self):

        assert self.is_not_element_present(*BasketPageLocators.STATUS)
