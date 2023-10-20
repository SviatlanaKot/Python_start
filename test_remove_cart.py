from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_form(driver, auth):

    button_add = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    button_add.click()
    time.sleep(3)

    cart = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart.click()
    time.sleep(3)

    assert len(driver.find_elements(By.CSS_SELECTOR, 'div[class="cart_item"]')) == 1

    button_remove = driver.find_element(By.CSS_SELECTOR, 'button[data-test="remove-sauce-labs-backpack"]')
    button_remove.click()
    time.sleep(3)

    assert len(driver.find_elements(By.CSS_SELECTOR, 'div[class="cart_item"]')) == 0

    # assert len(driver.find_element(By.CSS_SELECTOR, 'div.removed_cart_item')) == 0
    # assert driver.find_element(By.CSS_SELECTOR, 'div.removed_cart_item')

