# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math, time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    
    button_click = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)

    find_x =  browser.find_element(By.ID, "input_value")
    x = find_x.text

    y = calc(x)

    answer_input =  browser.find_element(By.ID, "answer").send_keys(y)

    button_answer =  browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()





finally:

	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла
