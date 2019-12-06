# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import math, time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")


def sum (x,y):
    return x + y

try:

    # найти числа в формуле
    a_find = browser.find_element(By.ID, "num1")
    b_find = browser.find_element(By.ID, "num2")

    # найденные значения сделать числами, а не строкой
    a = int(a_find.text)
    b = int(b_find.text)
    
    # посчитать формулу и сделать полученное значение строкой
    value = str(sum(a,b))

    # открыть выпадающий список
    select = Select(browser.find_element(By.ID, "dropdown"))
    # выбрать значение в списке, полученное из формулы
    select.select_by_value(value)


    # найти и нажать кнопку
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()



finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
