
import os, pickle

import pytest
from selenium.webdriver.chrome import webdriver

from pages.web_page import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements
from settings import project_url

# страница просмотра книги
class AboutBookPage(WebPage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

