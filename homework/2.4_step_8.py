from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()
    x = int(browser.find_element(By.ID, "input_value").text)


    def fun(x):
        return math.log(abs(12*math.sin(x)))


    y = fun(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()

    alert_text = browser.switch_to.alert.text
    print(alert_text.split(':')[-1])
    browser.switch_to.alert.accept()

finally:
    browser.quit()



