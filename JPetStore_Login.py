from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Login:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =======================================LOGIN PAGE========================================
    def username_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")

    def password_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')

    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='signon']")

    def create_new_user_button(self):
        return self.driver.find_element(By.LINK_TEXT, 'Register Now!')

    def sign_in_flow(self, username, password):
        self.username_element().send_keys(username)
        self.password_element().clear()
        self.password_element().send_keys(password)
        self.login_button().click()
    # =======================================LOGIN PAGE========================================





