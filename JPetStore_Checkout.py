from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait



class Checkout:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =======================================Checkout - Payment Details=======================================
    def card_type(self):
        card_type = self.driver.find_element(By.CSS_SELECTOR, 'select[name="order.cardType"]')
        card = Select(card_type)
        return card

    def card_number(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="order.creditCard"]')

    def expire_date(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="order.expiryDate"]')

    # =======================================Checkout - Billing Details=======================================

    def firstname(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="order.billToFirstName"]')

    def lastname(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="order.billToLastName"]')

    def address1(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="order.billAddress1"]')

    def address2(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="order.billAddress2"]')

    def city(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="order.billCity"]')

    def state(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="order.billState"]')

    def zip(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="order.billZip"]')

    def country(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="order.billCountry"]')

    def continue_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='newOrder']")

    def payment_flow(self, card_type, card_number, expire_date):
        self.card_number().clear()
        self.expire_date().clear()
        self.card_type().select_by_visible_text(card_type)
        self.card_number().send_keys(card_number)
        self.expire_date().send_keys(expire_date)
        self.continue_button().click()

    def confirm(self):
        return self.driver.find_element(By.CLASS_NAME, 'Button')

    def checkout_successful_msg(self):
        return self.driver.find_element(By.XPATH, "//ul[@class='messages']/li").text

    def copy_order_number(self):
        order_number = self.driver.find_element(By.XPATH, '//tr/th[@colspan="2"][@align="center"]')
        return order_number.text[7:12]






