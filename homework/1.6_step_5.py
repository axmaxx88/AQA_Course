import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Maksim")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Engineer")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Astrakhan")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()


