# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math, time, os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")



try:
    
    
    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("asfdasf")

    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("asshherg")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("ghj123ghfj")
   

    # загрузить файл в input
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    print(file_path)
      
    
    # найти элемент input и положить в него файл, который получили в file_path
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
      

finally:

	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла
