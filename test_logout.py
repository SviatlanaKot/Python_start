from selenium import webdriver
import selenium.webdriver.common.by
import time
import data


# driver = webdriver.Chrome()

def test_login_form(driver, logout):
    driver.get(data.MAIN_PAGE)

    url_before = driver.current_url
    time.sleep(5)
    url_after = driver.current_url

    assert url_before == url_after

# def test_login_form():
#
#     driver.get("https://www.saucedemo.com/")
#
#     url_before = driver.current_url
#
#     username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
#     username_field.send_keys('standard_user')
#
#     password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
#     password_field.send_keys('secret_sauce')
#
#     login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
#     login_button.click()
#     time.sleep(3)
#
#     burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
#     burger_menu.click()
#
#     logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
#     logout.click()
#
#     url_after = driver.current_url
#
#     assert url_before == url_after
