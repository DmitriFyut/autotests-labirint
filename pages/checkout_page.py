
import os, pickle

import pytest
from selenium.webdriver.chrome import webdriver

from pages.web_page import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements
from settings import checkout_page

# страница "Корзина"
class CheckoutPage(WebPage):
    def __init__(self, driver, url = ''):
        if not url:
            url = checkout_page
        super().__init__(driver, url)

    page_title = WebElement(WebPage, css_selector = 'div.checkout__header h1') # заголовок стрницы "Оформление заказа"