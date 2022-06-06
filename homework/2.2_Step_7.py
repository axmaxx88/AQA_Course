from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os  # download files

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys("Goga")
    browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys("Gogavich")
    browser.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("goga@mail.ru")
    # get the path to the directory of the current executable file:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # add filename to this path:
    file_path = os.path.join(current_dir, "test_file.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()

