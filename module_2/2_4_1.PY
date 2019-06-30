from selenium import webdriver

browser = webdriver.Chrome()
button = browser.find_element_by_id("button")
button.click()

