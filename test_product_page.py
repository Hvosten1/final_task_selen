import time

import pytest

from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import time # в начале файла


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        page.open()
        page.register_new_user(email, password)
        time.sleep(10)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        try:
            page = ProductPage(browser, link)
            page.open()
            page.click_purchase()
            page.solve_quiz_and_get_code()
            page.should_be_product_page()
        except:

            print(page.url)
            time.sleep(5)



    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


def test_guest_can_add_product_to_basket(browser):
    try:
        page = ProductPage(browser, link)
        page.open()
        page.click_purchase()
        page.should_be_product_page()
    except:

        print(page.url)
        time.sleep(5)



def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_purchase()
    page.should_not_be_success_message()





@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_purchase()
    time.sleep(1)
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    bu_page = BasketPage(browser, browser.current_url)
    bu_page.busket_is_empty()
    time.sleep(5)
