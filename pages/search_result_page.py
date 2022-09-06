
import os, pickle

import pytest
from selenium.webdriver.chrome import webdriver

from pages.web_page import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements


class SearchResultPage(WebPage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    # страница с результатами поиска (по умолчанию вкладка "Товары")
    authors_link = WebElement(WebPage, css_selector='a[data-id_tab="1"]')  # вкладка "Авторы"
    found_author = WebElement(WebPage, css_selector='a.rubric-list-item')  # первый автор в списке результатов

    # страница с результатами поиска (по умолчанию вкладка "Товары")
    book_name = WebElement(WebPage, css_selector='span.product-title')  # имя первого найденного товара (название книги)
    book_author = WebElement(WebPage, css_selector='div.product-author > a > span')  # имя автора первого найденного товара (автор книги)
    add_to_favorite = WebElement(WebPage, css_selector='.icon-fave.track-tooltip.js-open-deferred-block')  # кнопка "Отложить" у первого товара
    delete_from_favorite = WebElement(WebPage, css_selector='div.js-putorder-block-change.b-dropdown-window span.b-list-item-hover.pointer')
    add_to_cart = WebElement(WebPage, css_selector='div.product-buy.buy-avaliable.fleft a.btn.buy-link.btn-primary')  # кнопка "В корзину" у первого товара
    search_result_author = WebElement(WebPage, css_selector="a:nth-child(1) > span.rubric-item-name") # Первый результат поиска по автору
    # страница с ненайденным результатом поиска
    not_found_issue = WebElement(WebPage, css_selector='div.search-error h1')  # строка с сообщениемм 'Мы ничего не нашли по вашему запросу! Что делать?'
