import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
page = webdriver.Chrome()
page.get(link)
fname = page.find_element_by_css_selector(".form-control[name='firstname']")
sname = page.find_element_by_css_selector(".form-control[name='lastname']")
email = page.find_element_by_css_selector(".form-control[name='email']")
infile = page.find_element_by_id("file") # находим элемент input со значением атрибута type="file"
button = page.find_element_by_class_name("btn")
fname.send_keys("Dima")
sname.send_keys("Shumaev")
email.send_keys("alibaba@yahoo.com")
dir_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(dir_path, '2_2_3.txt')
infile.send_keys(file_path)
button.click()

