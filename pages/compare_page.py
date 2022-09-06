import os, pickle

import pytest
from selenium.webdriver.chrome import webdriver

from pages.web_page import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements
from settings import compare_url

# страница "Корзина"
class ComparetPage(WebPage):
    def __init__(self, driver, url = ''):
        if not url:
            url = compare_url
        super().__init__(driver, url)


    delete_compare_list_button = WebElement(WebPage, css_selector='div.compare-delete-list')  # кнопка удаления сравнительного списка книг
    empty_compare_text = WebElement(WebPage, css_selector='p.compare-text-empty')  # текст на старнице когда нет товаров для сравнения