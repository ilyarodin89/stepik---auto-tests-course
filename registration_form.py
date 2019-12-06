# -*- coding: utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration2.html")

name = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input.form-control.first")
name.send_keys("Ivan")
lastname = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input.form-control.second")
lastname.send_keys("Petrov")
mail = browser.find_element_by_css_selector("input.form-control.third")
mail.send_keys("email@pochta.ru")

#ниже поиск необязательных полей
#input4 = browser.find_element_by_css_selector("div.second_block > div.form-group.first_class > input.form-control.first")
#input4.send_keys("1488")
#input4 = browser.find_element_by_css_selector("div.second_block > div.form-group.second_class > input.form-control.second")
#input4.send_keys("Planet Erth")


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


