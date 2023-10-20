from selenium.webdriver.common.by import By

# AUTH

# USERNAME_FIELD = '//input[@data-test="username"]'
# PASSWORD_FIELD = '//input[@data-test="password"]'
# LOGIN_BUTTON = '//input[@data-test="login-button"]'

USERNAME_FIELD = (By.XPATH, '//input[@data-test="username"]')
PASSWORD_FIELD = (By.XPATH, '//input[@data-test="password"]')
LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-button"]')


