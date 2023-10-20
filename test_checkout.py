from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_checkout_form(driver, auth):

    button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    button.click()
    time.sleep(3)

    cart = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart.click()
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, 'button[data-test="checkout"]').click()

    driver.find_element(By.CSS_SELECTOR, 'input[data-test="firstName"]').send_keys('Olya')
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="lastName"]').send_keys('Zyk')
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="postalCode"]').send_keys('5241')

    driver.find_element(By.CSS_SELECTOR, 'input[data-test="continue"]').click()
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, 'button[data-test="finish"]').click()

    assert driver.find_element(By.CSS_SELECTOR, 'h2.complete-header').text == 'Thank you for your order!'




