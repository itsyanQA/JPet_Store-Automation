from selenium import webdriver
from selenium.webdriver.common.by import By

class Categories:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # =================================ITEM SELECTION===============================
    def fish_items(self, index):
        fish_items = self.driver.find_elements(By.XPATH, '//table/tbody/tr/td/a')
        return fish_items[index]

    def dog_items(self, index):
        dog_items = self.driver.find_elements(By.XPATH, '//table/tbody/tr/td/a')
        return dog_items[index]

    def reptile_items(self, index):
        reptile_items = self.driver.find_elements(By.XPATH, '//table/tbody/tr/td/a')
        return reptile_items[index]

    def cat_items(self, index):
        cat_items = self.driver.find_elements(By.XPATH, '//table/tbody/tr/td/a')
        return cat_items[index]

    def birds_items(self, index):
        cat_items = self.driver.find_elements(By.XPATH, '//table/tbody/tr/td/a')
        return cat_items[index]

    # ===========================================================================
    def product_id_seeker(self, index):
        product_ids = self.driver.find_elements(By.XPATH, '//table/tbody/tr/td/a')
        return product_ids[index].text

    def item_id_seeker(self, index):
        item_ids = self.driver.find_elements(By.XPATH, '//tr/td[1]')
        new_item_ids = item_ids[:-1]
        return new_item_ids[index].text

    def item_description(self, index):
        description = self.driver.find_elements(By.XPATH, '//tr/td[3]')
        return description[index].text

    def list_price(self, index):
        list_price = self.driver.find_elements(By.XPATH, '//tr/td[4]')
        list_price = list_price[index].text
        return list_price[1:]

    def add_to_cart(self, index):
        add_to_cart_list = self.driver.find_elements(By.CLASS_NAME, 'Button')
        return add_to_cart_list[index]








