from selenium import webdriver
import time
import unittest

link = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]
expectedResult = "Поздравляем! Вы успешно зарегистировались!"

class unitTestUse(unittest.TestCase):
    def test1(self):
        self.assertEqual(testCase(link[0]), expectedResult, "Test fall down")
    def test2(self):
        self.assertEqual(testCase(link[1]), expectedResult, "Test fall down")


def testCase(link):
    mass_of_class = ['first','second','third']
    browser = webdriver.Chrome()
    browser.get(link)
    for i in mass_of_class:
        selector = str("input." + i + r"[required='']")
        element = browser.find_element_by_css_selector(selector)
        element.send_keys("tyty")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    return welcome_text

if __name__ == "__main__":
    unittest.main()
