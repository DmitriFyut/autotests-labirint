
import os, pickle

import pytest
from selenium.webdriver.chrome import webdriver

from pages.web_page import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements
from settings import favorites_url

# страница "Отложенные товары"
class FavoritesPage(WebPage):
    def __init__(self, driver, url = ''):
        if not url:
            url = favorites_url
        super().__init__(driver, url)


    clear_favorite = WebElement(WebPage, link_text='Очистить')  # кнопка "Очистить"
    message = WebElement(WebPage, css_selector='div#messages-text p.g-alttext-small')  # сообщение "Выбранные товары удалены"
    no_favorite_goods = WebElement(WebPage, id='cabinet') # текст на случай если нет отложенных товаров