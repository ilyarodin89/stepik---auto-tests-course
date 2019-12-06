# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    button_book = browser.find_element(By.ID, "book")

    # ждем, пока не появится цена  в 100$
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))

    button_book.click()

	
	#price = WebDriverWait(browser, 2).until(
	       # EC.text_to_be_present_in_element((By.ID, "input_value"),"$100")
	  #  )



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
    browser.find_element(By.ID, "solve").click()



finally:

	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

	# не забываем оставить пустую строку в конце файла

