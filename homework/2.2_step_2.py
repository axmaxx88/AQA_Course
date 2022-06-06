from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    time.sleep(0.5)
    select.select_by_value("46")
    time.sleep(0.5)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(5)
    browser.quit()




