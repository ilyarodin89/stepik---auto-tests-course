# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math, time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try:
    
    # найти число
    find_x = browser.find_element(By.ID, "input_value")

    # найденные значения сделать числами, а не строкой
    x = int(find_x.text)

    # посчитать формулу
    y = calc(x)

    # проскролить страницу внизу до формы ввода
    input_val = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_val)
    # кликнуть по элементу ввода
    input_val.click()
    # ввести значение из формулы в форму
    input_val.send_keys(y)

    # находим чекбокс и кликаем по нему
    browser.find_element(By.ID, "robotCheckbox").click()

    # находим нужный радиобаттон и кликаем
    browser.find_element(By.ID, "robotsRule").click()

    # находим и нажимаем кнопку Отправить
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()







finally:

	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла