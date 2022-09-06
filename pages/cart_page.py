
import os, pickle

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.web_page import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements
from settings import cart_url

# страница "Корзина"
class CartPage(WebPage):
    def __init__(self, driver, url = ''):
        if not url:
            url = cart_url
        super().__init__(driver, url)

    # страница Корзина
    empty_cart_text = WebElement(WebPage, css_selector = 'form#basket-step1-default span.g-alttext-small.g-alttext-grey.g-alttext-head')  # сообщение "Ваша корзина пуста"
    go_to_checkout_button = WebElement(WebPage, css_selector = 'button.btn.btn-primary.btn-large.fright.start-checkout-js') # кнопка "Перейти к оформлению"
    item_reduction_button = WebElement(WebPage, css_selector = 'div.product-operations span.btn.btn-lessen.btn-lessen-cart') # кнопка минус
    item_increase_button = WebElement(WebPage, css_selector = 'div.product-operations span.btn.btn-increase.btn-increase-cart') # кнопка плюс
    goods_quantity_input = WebElement(WebPage, css_selector = 'input.quantity')

    empty_cart_button = WebElement(WebPage, css_selector = 'div.text-regular.empty-basket-link a') # кнопка "Очистить корзину"
    go_to_checkout_buttont = WebElement(WebPage, css_selector = 'button.btn.btn-primary.btn-large.fright.start-checkout-js')
    name_input = WebElement(WebPage, css_selector = 'input[placeholder="Имя"]')
    surname_input = WebElement(WebPage, css_selector = 'input[placeholder="Фамилия"]')
    phone_input = WebElement(WebPage, css_selector = 'input[placeholder="Мобильный телефон"]')
    email_input = WebElement(WebPage, css_selector = 'input[placeholder="Электронная почта"]')

    checkout_button = WebElement(WebPage, css_selector = 'div.base-button.set-min-width.base-button--theme-red.base-button--noselect.no-active-effect.no-hover-effect.footer__desktop-checkout-btn.margin-set.padding-set')
    text_under_name_input = WebElement(WebPage, css_selector = 'div.first-name div.text-xs.css-default')
    text_under_surname_input = WebElement(WebPage, css_selector = 'div.last-name div.text-xs.css-default')
    text_under_phone_input = WebElement(WebPage, css_selector = 'div.phone div.text-xs.css-default')
    text_under_email_input = WebElement(WebPage, css_selector = 'div.email div.text-xs.css-default')

    def get_phone_input(self, driver):
        element = driver.find_element_by_css_selector('input[placeholder="Мобильный телефон"]')
        return element

    def get_email_input(self, driver):
        element = driver.find_element_by_css_selector('input[placeholder="Электронная почта"]')
        return element