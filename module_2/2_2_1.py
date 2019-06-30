from selenium import webdriver
buff = 0
page = webdriver.Chrome()
page.get("http://suninjuly.github.io/selects1.html")
#options = page.find_elements_by_teg("option")
#for option in options:
#    buff += option.get_attribute("value")
#for option in options:
#    if buff == int(option.get_attribute("value")):
#        option.click()
#        break
num1 = int(page.find_element_by_id("num1").text)
num2 = int(page.find_element_by_id("num2").text)
num = str(num1 + num2)
print(num)
options = page.find_elements_by_tag_name("option")
for option in options:
   if num == option.get_attribute("value"):
        option.click()
        break
button = page.find_element_by_css_selector("[type='submit']")
button.click()
