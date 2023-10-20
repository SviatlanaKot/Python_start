import time
from selenium.webdriver.common.by import By


def test_registration(driver):
    driver.get('https://victoretc.github.io/webelements_information/')
    state = driver.find_element(By.CSS_SELECTOR, '#registerButton').is_enabled()
    print(state)
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('Ola')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Zuk')
    check_box = driver.find_element(By.CSS_SELECTOR, '#agreement')
    print(check_box.is_selected())
    check_box.click()
    time.sleep(3)
    print(check_box.is_selected())
    time.sleep(3)
    state = driver.find_element(By.CSS_SELECTOR, '#registerButton').is_enabled()
    print(state)
    assert state is True
    driver.find_element(By.CSS_SELECTOR, '#registerButton').click()
    assert driver.current_url == 'https://victoretc.github.io/webelements_information/?'









