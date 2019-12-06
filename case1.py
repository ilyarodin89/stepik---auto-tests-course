from selenium import webdriver

#Получаем в переменную указатель на браузер
browser.webdriver.Firefox()

# Переход на ресурс
browser.get('ссылка на сайт')

# Получаем указатель на поле ввода логина
textarea=browser.find_element_by_css_selector('#index_email')
# печатаем текст в поле ввода
textarea.send_keys('текст')

# Получаем указатель на поле ввода пароля
textarea=browser.find_element_by_css_selector('#index_pass')
# печатаем пароль
textarea.send_keys('текст')

# Получаем указатель на кнопку "Войти"
submit=browser.find_element_by_css_selector('#index_login_button')
# Нажимаем кнопку Войти
submit.click()