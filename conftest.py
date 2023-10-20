import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import *
from locators import *



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def auth(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()



# @pytest.fixture
# def logout(driver, auth):
#     burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
#     burger_menu.click()
#
#     logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
#     logout.click()
