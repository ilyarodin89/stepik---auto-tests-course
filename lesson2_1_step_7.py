# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math, time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try:
	# 2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
	treasure = browser.find_element(By.ID, "treasure")
	# 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
	x = treasure.get_attribute("valuex")
	# 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
	y = calc(x)

	# 5. Ввести ответ в текстовое поле.
	input_val = browser.find_element(By.ID, "answer")
	input_val.send_keys(y)

	# 6. Отметить checkbox "I'm the robot".
	checkbox_robo = browser.find_element(By.ID, "robotCheckbox").click()

	# 7. Выбрать radiobutton "Robots rule!".
	rario_robo = browser.find_element(By.ID, "robotsRule").click()

	# 8. Нажать на кнопку "Submit".
	button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()

finally:

	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла
