# -*- coding: utf-8 -*-

from selenium import webdriver
import math, time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector("input.form-control")
input.send_keys(y)
checkbox = browser.find_element_by_css_selector("#robotCheckbox.form-check-input").click()
radio = browser.find_element_by_css_selector("#robotsRule.form-check-input").click()
button = browser.find_element_by_css_selector("button.btn.btn-default").click()

