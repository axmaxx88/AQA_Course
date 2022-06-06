from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(2)").text)
    y = int(browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(4)").text)


    def summ(x, y):
        return str(x + y)


    z = summ(x, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(5)
    browser.quit()

