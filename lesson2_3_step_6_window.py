# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math, time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try:
    
    #находим кнопку и нажимаем
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary").click()

    #new_window = browser.window_handles

    #print(new_window)

    #time.sleep(10)

    #первое окно первое
    first_window = browser.window_handles[0]
    
    #новое окно второе
    new_window = browser.window_handles[1]

    #переходим на новую вкладку
    browser.switch_to.window(new_window)


    # найти число
    find_x = browser.find_element(By.ID, "input_value")

    # найденные значения сделать числами, а не строкой
    x = int(find_x.text)

    # посчитать формулу
    y = calc(x)

    
    input_val = browser.find_element(By.ID, "answer")
    
    # ввести значение из формулы в форму
    input_val.send_keys(y)

    
    # находим и нажимаем кнопку Отправить
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()







finally:

	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла