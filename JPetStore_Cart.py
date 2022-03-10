from selenium import webdriver
from selenium.webdriver.common.by import By

class Cart:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def remove_item(self, index):
        remove_list = self.driver.find_elements(By.XPATH, "//td/a[@class='Button']")
        return remove_list[index]

    def update_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='updateCartQuantities']")

    def proceed_to_checkout(self):
        return self.driver.find_element(By.LINK_TEXT, 'Proceed to Checkout')

    def quantity_element(self, row):
        quantitys = self.driver.find_elements(By.XPATH, "//td/input[@type='text']")
        return quantitys[row]

    def quantity_changer_flow(self, row, quantity):
        self.quantity_element(row).clear()
        self.quantity_element(row).send_keys(quantity)
        self.update_cart()

    def qty_sum(self):
        qty_total = self.driver.find_elements(By.XPATH, "//td/input[@type='text']")
        sum1 = 0
        for i in qty_total:
            sum1 += int(i.get_attribute('value'))
        return str(sum1)

    def item_id_by_row(self, row):
        item_ids = self.driver.find_elements(By.XPATH, "//td[1]/a")
        return item_ids[row].text

    def product_id_by_row(self, row):
        product_ids = self.driver.find_elements(By.XPATH, "//tr/td[2]")
        product_ids_filtered = product_ids[:-1]
        return product_ids_filtered[row].text

    def description_by_row(self, row):
        descriptions = self.driver.find_elements(By.XPATH, "//tr/td[3]")
        return descriptions[row].text

    def list_price_by_unit(self, row):
        list_price = self.driver.find_elements(By.XPATH, "//tr/td[6]")
        list_price = list_price[row].text
        return list_price[1:]

    def total_cost_by_row(self, row):
        list_price = self.driver.find_elements(By.XPATH, "//tr/td[7]")
        list_price = list_price[row].text
        return list_price[1:]

    def sub_total(self):
        subtotal = self.driver.find_element(By.CSS_SELECTOR, "td[colspan='7']")
        for i in range(len(subtotal.text)):
            if ',' in subtotal.text:
                subtotal.text.replace(',', '')
        return subtotal.text[12:]

    def qty_per_row(self, row):
        qtys = self.driver.find_elements(By.XPATH, "//td/input[@type='text']")
        return qtys[row].get_attribute('value')

    def multiply_qty_by_list_price(self, row):
        qty = self.qty_per_row(row)
        list_price = self.list_price_by_unit(row)
        calculation = float(qty) * float(list_price)
        return "{:.2f}".format(calculation)

    def global_qty_by_list_price(self, row1, row2, row3):
        qtys = self.driver.find_elements(By.XPATH, "//td/input[@type='text']")
        list_price = self.driver.find_elements(By.XPATH, "//tr/td[6]")
        first_calculation = float(qtys[row1].get_attribute('value')) * float(list_price[row1].text[1:])
        second_calculation = float(qtys[row2].get_attribute('value')) * float(list_price[row2].text[1:])
        third_calculation = float(qtys[row3].get_attribute('value')) * float(list_price[row3].text[1:])
        total = first_calculation + second_calculation + third_calculation
        return "{:,.2f}".format(total)

    def global_descriptions(self):
        descriptions = self.driver.find_elements(By.XPATH, "//tr/td[3]")
        empty_string = ''
        for i in descriptions:
            empty_string += i.text
        return empty_string

    def shopping_cart_text(self):
        return self.driver.find_element(By.XPATH, "//div[@id='Cart']/h2").text

    def cart_empty(self):
        return self.driver.find_element(By.XPATH, "//tr/td/b").text

    def total_cost_element(self, row):
        total = self.driver.find_elements(By.XPATH, "//tr/td[7]")
        return total[row].text







