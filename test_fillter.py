from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

def test_login_form():

    driver.get("https://www.saucedemo.com/")

    url_before = driver.current_url

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(3)

    items_before = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item_name')
    print(len(items_before))
    list_before = []
    for x in items_before:
        list_before.append(x.text)
        print(x.text)

    button_filter = Select(driver.find_element(By.CSS_SELECTOR, 'select[data-test="product_sort_container"]'))
    button_filter.select_by_index(1)
    time.sleep(3)

    items = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item_name')
    print(len(items))
    list_after = []
    for x in items:
        list_after.append(x.text)
        print(x.text)

    assert list_after == sorted(list_before, reverse=True)






