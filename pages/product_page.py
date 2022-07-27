from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_url()
        self.equals_names()
        self.equals_prices()
        # self.should_not_be_success_message()

    def should_be_product_url(self):
        assert 'promo' in self.url, "It's not product page"
        assert True

    def equals_names(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        pname = self.browser.find_element(*ProductPageLocators.PURCHASE_NAME).text
        assert name == pname, "Wrong purchase name"

    def equals_prices(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        pprice = self.browser.find_element(*ProductPageLocators.BUCKET_TOTAL).text
        assert price == pprice, "Wrong prices"

    def click_purchase(self):
        sub_elem = self.browser.find_element(*ProductPageLocators.PURCHASE_BUTTON)
        sub_elem.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PURCHASE_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PURCHASE_NAME), \
            "Block pressented, but it must be dissapeared"
