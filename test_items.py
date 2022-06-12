from selenium.webdriver.common.by import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form .btn")
    assert basket_button, "The page doesn't have an 'Add to basket button'"

