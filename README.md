# final-autotests-labirint
# В данном репозитории представлено ряд автотестов для интернет-магазина лабиринт https://www.labirint.ru/ с
Python и фреймворка Selenium. Для запусков тестов необходимо установить фреймворк selenium(pytest-selenium) 

В рамках данного проекта автоматизированы основные сценарии пользователей:
* авторизация на сайте
* поиск автора
* поиск книги по названию
* поиск книги по ISBN
* добавление книги в Отложенные
* добавление книги в Корзину
* оформление покупки
* отправки вопроса в поддержку
* проверена работоспособность части ссылок на главной странице

Как запустить:

Скачать драйвер для Chrome: https://chromedriver.chromium.org/downloads
 или  Firefox: https://github.com/mozilla/geckodriver/releases

Установите все необходимые библиотеки пакетов Python

Откройте Терминал

Запустите в терминале строку:

python -m pytest -v --driver Chrome --driver-path /path/to//chromedriver.exe

Теперь каждый раз для запуска тестов необходимо указать, какой именно браузер мы хотим использовать, и путь к его драйверу (не забываем заменить /path/to/ на свой путь):

pytest -v --driver Chrome --driver-path /path/to//chromedriver.exe
или

pytest --driver Firefox --driver-path /path/to/geckodriver.exe 

или Запустите нажатием соответствующей кнопки с помощью RUN файл: pytest in test_for_labirint.py

Приятного тестирования)


