from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from math import log, sin


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
browser.find_element_by_id("book").click()
x = int(browser.find_element_by_id("input_value").text)
y = str(log(abs(12*sin(x))))
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()
