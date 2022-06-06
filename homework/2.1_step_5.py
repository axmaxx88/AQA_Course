from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "div span#input_value")
    x = x_element.text


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)
    time.sleep(2)
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    input2.click()
    time.sleep(2)
    input3 = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    input3.click()
    time.sleep(2)
    input4 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    input4.click()

finally:
    time.sleep(15)
    browser.quit()






