from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.CSS_SELECTOR, "label span:nth-child(2)").text)

    def fun(x):
        return math.log(abs(12 * math.sin(x)))

    y = fun(x)
    answer_field = browser.find_element(By.ID, "answer")
    # we passed the text of JS_script and found element 'button' to the method "execute_script" to scroll the page
    # to 'button' element:
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
    answer_field.send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(15)
    browser.quit()



