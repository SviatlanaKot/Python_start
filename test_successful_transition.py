from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_login_form():

    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(3)

    text_before = driver.find_element(By.ID, 'item_4_title_link').text

    img = driver.find_element(By.CSS_SELECTOR, 'img[alt="Sauce Labs Backpack"]')
    img.click()
    time.sleep(3)

    text_after = driver.find_element(By.CLASS_NAME,'inventory_details_name large_size').text
    assert text_before == text_after
    




