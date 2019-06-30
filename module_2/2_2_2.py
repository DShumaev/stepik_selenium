from selenium import webdriver
from math import log, sin

page = webdriver.Chrome()
page.get("https://suninjuly.github.io/execute_script.html")
x = int(page.find_element_by_id("input_value").text)
y = str(log(abs(12*sin(x))))
answer = page.find_element_by_id("answer")
page.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(y)
checkbox = page.find_element_by_id("robotCheckbox")
page.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()
radio = page.find_element_by_id("robotsRule")
page.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()
button = page.find_element_by_class_name("btn")
page.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()















