from selenium import webdriver
import selenium.webdriver.common.by
import time
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from data import LOGIN, PASSWORD, MAIN_PAGE


# def test_login_form():
#
#     driver.get("https://www.saucedemo.com/")
#
#     username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
#     username_field.send_keys('standard_user')
#
#     password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
#     password_field.send_keys('secret_sauce')
#
#     login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
#     login_button.click()
#
#     time.sleep(5)
#     assert driver.current_url == "https://www.saucedemo.com/inventory.html"
#
#     driver.quit()

def test_login_form(driver):

    driver.get(MAIN_PAGE)
    driver.find_element(selenium.webdriver.common.by.By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(selenium.webdriver.common.by.By.XPATH, PASSWORD_FIELD).send.keys(PASSWORD)
    driver.find_element(selenium.webdriver.common.by.By.XPATH, LOGIN_BUTTON).click()

    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


