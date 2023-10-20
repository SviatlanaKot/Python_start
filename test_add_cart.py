from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_form(driver, auth):

    text_before = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"]').text

    button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    button.click()
    time.sleep(3)

    cart = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart.click()
    time.sleep(3)

    text_after = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"]').text
    assert text_before == text_after
