# -*- coding: utf-8 -*-

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time


def calc(x):
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",\
    "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1",\
    "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_find_message_on_page(browser, links):
    #передаем ссылки из параметров для открытия в браузере
    browser.get(f"{links}")

    
    print("открыл браузер")
    #находим форму для ответа

    answer_form = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.textarea.string-quiz__textarea.ember-text-area.ember-view")))

    #answer_form = browser.find_element(By.CSS_SELECTOR, "textarea.textarea.string-quiz__textarea.ember-text-area.ember-view")



    print("нашел форму ввода")

    answer = str(calc)

    #вставляем в форму для ответа значение из формулы
    answer_form.send_keys(answer)

    #находим кнопку отправки ответа и нажимаем
    button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()

    # ждем 5 секунд, пока не появится слово "Correct!"
    text_successful = WebDriverWait(browser,5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "pre.smart-hints__hint"),"Correct!"))

    assert "Correct!" in text_successful.text, "!!!!!ТЕКСТ НЕ НАЙДЕН!!!!!"











