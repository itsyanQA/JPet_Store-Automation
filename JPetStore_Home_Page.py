from selenium import webdriver
from selenium.webdriver.common.by import By


class Home_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def Fish_Left(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'img[src="../images/fish_icon.gif"]')

    def Dogs_Left(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'img[src="../images/dogs_icon.gif"]')

    def Cats_Left(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'img[src="../images/cats_icon.gif"]')

    def Reptiles_Left(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'img[src="../images/reptiles_icon.gif"]')

    def Birds_Left(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'img[src="../images/birds_icon.gif"]')
    # ==============================================================================================

    def Fish_Picture(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'area[alt=Fish]')

    def Dogs_Picture(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'area[alt=Dogs]')

    def Cats_Picture(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'area[alt=Cats]')

    def Reptiles_Picture(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'area[alt=Reptiles]')

    def Birds_Picture(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'area[alt=Birds]')

    def Big_Bird(self):
        return self.driver.find_element(By.XPATH, "//area[@alt='Birds'][@coords='72,2,280,250']")

    # ==============================================================================================
    def Fish_Top(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='QuickLinks']>a>img[src='../images/sm_fish.gif']")

    def Dogs_Top(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='QuickLinks']>a>img[src='../images/sm_dogs.gif']")

    def Cats_Top(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='QuickLinks']>a>img[src='../images/sm_cats.gif']")

    def Reptiles_Top(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='QuickLinks']>a>img[src='../images/sm_reptiles.gif']")

    def Birds_Top(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='QuickLinks']>a>img[src='../images/sm_birds.gif']")

    # ==============================================================================================

    def SearchBar(self):
        return self.driver.find_element(By.NAME, 'keyword')

    def SearchButton(self):
        return self.driver.find_element(By.NAME, 'searchProducts')

    def Search_flow(self, value):
        self.SearchBar().send_keys(value)
        self.SearchButton().click()

    def Home_Page_Button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "img[src='../images/logo-topbar.gif']")

    def Hit_Search_Button(self):
        self.SearchButton().click()

    def Enter_Fish_Left(self):
        self.Fish_Left().click()

    def Enter_Dogs_Left(self):
        self.Dogs_Left().click()

    def Enter_Cats_Left(self):
        self.Cats_Left().click()

    def Enter_Reptiles_Left(self):
        self.Reptiles_Left().click()

    def Enter_Birds_Left(self):
        self.Birds_Left().click()

    def about_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[id=MenuContent]>a[href='../help.html']")

    def sign_in(self):
        return self.driver.find_element(By.LINK_TEXT, "Sign In")

    def cart(self):
        return self.driver.find_element(By.NAME, "img_cart")

    def sign_out(self):
        return self.driver.find_element(By.LINK_TEXT, 'Sign Out')

    def my_account(self):
        return self.driver.find_element(By.LINK_TEXT, 'My Account')

    def my_orders(self):
        return self.driver.find_element(By.LINK_TEXT, 'My Orders')

    def order_number_by_row(self, row):
        orders = self.driver.find_elements(By.XPATH, '//tr/td[1]')
        print(orders[-1].text)
        return orders[row].text

    def account_user_id_text(self):
        user_id = self.driver.find_elements(By.XPATH, "//tr[1]/td[2]")
        return user_id[0].text

    def sign_in_existing_header(self):
        return self.driver.find_element(By.XPATH, "//form/p[1]").text





