from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Account:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =======================================REGISTRATION PAGE - User Info========================================

    def user_id(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")

    def password(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')

    def repeat_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="repeatedPassword"]')

    # =======================================REGISTRATION PAGE - Account Info=======================================

    def firstname(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.firstName"]')

    def lastname(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.lastName"]')

    def email(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.email"]')

    def phone(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.phone"]')

    def address1(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.address1"]')

    def address2(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.address2"]')

    def city(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.city"]')

    def state(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.state"]')

    def zip(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.zip"]')

    def country(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.country"]')

    # =======================================REGISTRATION PAGE - Profile Info=======================================

    def language_preference(self):
        language_preference = self.driver.find_element(By.CSS_SELECTOR, 'select[name="account.languagePreference"]')
        preference = Select(language_preference)
        return preference

    def favourite_category(self):
        favourite_category = self.driver.find_element(By.CSS_SELECTOR,
                                                      'select[name="account.favouriteCategoryId"]')
        category = Select(favourite_category)
        return category

    def my_list_checkbox(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.listOption"]')

    def my_banner_checkbox(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="account.bannerOption"]')

    def save_account_info(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="newAccount"]')

        # =======================================Registration Flow========================================

    def registration_flow(self, userid, newpassword, cnfrmpw, fname, lname, email,
                          phone, address1, address2, city, state, zip, country, lperference, fcategory):
        self.user_id().send_keys(userid)
        self.password().send_keys(newpassword)
        self.repeat_password().send_keys(cnfrmpw)
        self.firstname().send_keys(fname)
        self.lastname().send_keys(lname)
        self.email().send_keys(email)
        self.phone().send_keys(phone)
        self.address1().send_keys(address1)
        self.address2().send_keys(address2)
        self.city().send_keys(city)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="account.city"]')))
        self.state().send_keys(state)
        self.zip().send_keys(zip)
        self.country().send_keys(country)
        self.language_preference().select_by_visible_text(lperference)
        self.favourite_category().select_by_visible_text(fcategory)
        self.my_list_checkbox().click()
        self.my_banner_checkbox().click()
        self.save_account_info().click()