import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def auth(driver):
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()


@pytest.fixture(scope='function')
def logout(driver, auth):
    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()

    logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout.click()
