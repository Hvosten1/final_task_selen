import time

import pytest

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]


@pytest.mark.parametrize('link', links)
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    try:
        page = ProductPage(browser, link)
        page.open()
        page.click_purchase()
        page.solve_quiz_and_get_code()
        page.should_be_product_page()
    except:

        print(page.url)
        time.sleep(5)


@pytest.mark.parametrize('link', links)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_purchase()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', links)
@pytest.mark.skip
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', links)
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_purchase()
    time.sleep(1)
    page.should_be_disappeared()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
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
