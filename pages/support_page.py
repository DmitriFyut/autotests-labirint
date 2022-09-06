
import os, pickle

import pytest
from selenium.webdriver.chrome import webdriver

from pages.web_page import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements
from settings import support_url

# страница "Отложенные товары"
class SupportPage(WebPage):
    def __init__(self, driver, url = ''):
        if not url:
            url = support_url
        super().__init__(driver, url)

    logo = WebElement(WebPage, css_selector='a.b-header-b-logo-e-logo-wrap')
    ask_support_button = WebElement(WebPage, css_selector = 'a.support-question.sm-greater') # кнопка "Задать вопрос"
    posted_question = WebElement(WebPage, css_selector = 'div.message-text') # отправленный вопрос
    no_correspondence_text = WebElement(WebPage, css_selector = 'div.count-0')
    my_question_link = WebElement(WebPage, css_selector = 'div.top-support.max-width a.support-my') # ссылка в верхнем меню "Мои вопросы"
    search_here_input = WebElement(WebPage, css_selector = 'form#search_support input') # строка поиска сообщений
    submit_request_button = WebElement(WebPage, css_selector = 'form#search_support span')  # кнпокпа отправления запроса

    found_message =  WebElement(WebPage, css_selector = 'div.topic div.message-text')
    not_found_messages_text = WebElement(WebPage, css_selector = 'div.topics div.count-0')
    # модальная страница для авторизации
    find_login = WebElement(WebPage, css_selector='.full-input__input.formvalidate-error')  # поле для ввода логина (тел, емэйл, код скидки)
    input_button = WebElement(WebPage, id='g-recap-0-btn')  # кнопка "Войти"

    # модальная страница "Мой вопрос"
    textarea_for_question = WebElement(WebPage, css_selector = 'div.support_add__form-block-side.support_add__form-block-right textarea.support_add__form-msg.js-support-msg')
    send_question_button = WebElement(WebPage, css_selector = 'input[value="Отправить вопрос в Лабиринт"]') # кнопка "Отправить вопрос в Лабиринт"

