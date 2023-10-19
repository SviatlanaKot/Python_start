from selenium import webdriver
from selenium.webdriver.common.by import By
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

    button_add = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    button_add.click()
    time.sleep(3)

    cart = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart.click()
    time.sleep(3)

    button_remove = driver.find_element(By.CSS_SELECTOR, 'button[data-test="remove-sauce-labs-backpack"]')
    button_remove.click()
    time.sleep(3)

    # assert len(driver.find_element(By.CSS_SELECTOR, 'div[class="cart_list"]')) == 0
    # assert len(driver.find_element(By.CSS_SELECTOR, 'div.removed_cart_item')) == 0
    assert driver.find_element(By.CSS_SELECTOR, 'div.removed_cart_item')

