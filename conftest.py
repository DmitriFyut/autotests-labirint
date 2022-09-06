# Для дополнительной настройки работы браузера (размер окна, режим отображения и так далее), рекомендуется
# использовать фикстуры. Их стоит вставлять в файл conftest.py, который находится в корневой директории тестового
# проекта.

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from settings import valid_email, valid_password, project_url


@pytest.fixture(scope='function')
def driver():
    capabilities = DesiredCapabilities().CHROME
    capabilities["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome('../drivers/chromedriver', desired_capabilities=capabilities)
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()


@pytest.fixture(scope='function')
def driver_with_cookies(driver):
    response = requests.post(url=f"{project_url}/login", data={"email": valid_email, "pass": valid_password})
    assert response.status_code == 200
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print('\n getting auth_key')
    driver.get(project_url)
    cookie_list = response.request.headers.get('Cookie').split('=')
    driver.add_cookies({'name': cookie_list[0], 'value': cookie_list[1]})
    yield driver

