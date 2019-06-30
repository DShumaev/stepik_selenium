from selenium import webdriver
from math import log, sin

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_class_name("btn").click()
confirm = browser.switch_to.alert
confirm.accept()
x = int(browser.find_element_by_id("input_value").text)
y = str(log(abs(12*sin(x))))
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_class_name("btn").click()

