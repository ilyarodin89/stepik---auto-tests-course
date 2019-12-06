# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)


input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name(value2)
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name(value3)
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id(value4)
input4.send_keys("Russia")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

"""button = browser.find_element_by_xpath("//button[@class='btn'][contains(text(), 'Отправить')]")
button.click()"""




