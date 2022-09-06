import os, pickle

import pytest
from selenium.webdriver.chrome import webdriver

from pages.web_page import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements


# страница просмотра информации о книге
class AboutBookPage(WebPage):
    def __init__(self, driver, url):
        super().__init__(driver, url)


    isbn = WebElement(WebPage, css_selector='div.isbn')  # номер isbn книги
    add_to_cart = WebElement(WebPage, css_selector='a#buyto-buyids') # кнопка "Добавить в корзину"