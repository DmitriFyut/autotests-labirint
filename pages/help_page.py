import os, pickle

import pytest
from selenium.webdriver.chrome import webdriver

from pages.web_page import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements
from settings import help_url

# страница "Отложенные товары"
class HelpPage(WebPage):
    def __init__(self, driver, url = ''):
        if not url:
            url = help_url
        super().__init__(driver, url)


    logo = WebElement(WebPage, css_selector='a.b-header-b-logo-e-logo-wrap')
    search_input =  WebElement(WebPage, css_selector = 'input#txtwordsadv') # строка поиска сообщений
    find_button = WebElement(WebPage, css_selector = 'input[value="Найти"]') # кнопка Найти
    found_post_head = WebElement(WebPage, css_selector = 'div.p10 span.helpcard-head') # заголовок найденной статьи
    found_post_body_preview = WebElement(WebPage, css_selector = 'div.p10 p') # превью найденной статьи
    not_found_post_message = WebElement(WebPage, css_selector = 'div#messages-text')





