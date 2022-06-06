from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element(By.ID, "input_value").text)


    def fun(x):
        return math.log(abs(12*math.sin(x)))


    y = fun(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    alert_text = browser.switch_to.alert.text
    print(alert_text.split(': ')[-1])
    browser.switch_to.alert.accept()
    browser.quit()


