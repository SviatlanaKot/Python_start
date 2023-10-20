from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_login_form(driver, auth):

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






