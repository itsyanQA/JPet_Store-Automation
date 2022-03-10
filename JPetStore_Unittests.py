from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from JPetStore_Account import Account
from JPetStore_Home_Page import Home_Page
from JPetStore_Categories import Categories
from JPetStore_Login import Login
from JPetStore_Cart import Cart
from JPetStore_Checkout import Checkout


class JPetStore_Unittests(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.acc = Account(self.driver)
        self.categories = Categories(self.driver)
        self.login = Login(self.driver)
        self.homepage = Home_Page(self.driver)
        self.cart = Cart(self.driver)
        self.checkout = Checkout(self.driver)

    def test_1_task(self):
        '''Add 2 different items to the cart and change their quantity, assert that the quantity is true in the cart'''
        self.homepage.Reptiles_Top().click()
        self.categories.reptile_items(1).click()
        self.categories.add_to_cart(0).click()
        self.homepage.Home_Page_Button().click()
        self.homepage.Cats_Left().click()
        self.categories.cat_items(1).click()
        self.categories.add_to_cart(1).click()
        self.homepage.cart().click()
        self.cart.quantity_changer_flow(1, 5)
        self.assertEqual(self.cart.qty_sum(), '6')

    def test_2_task(self):
        '''add 3 different items to the cart, assert that the product item_id, product_id, description and unit price
        matches correctly in the cart, and multiply each item quantity by their unit price and assert that the
        subtotal is correct.'''
        self.homepage.Reptiles_Top().click()
        product_id1 = self.categories.product_id_seeker(1)
        self.categories.reptile_items(1).click()
        item_id1 = self.categories.item_id_seeker(0)
        description1 = self.categories.item_description(0)
        unit_price1 = self.categories.list_price(0)
        self.categories.add_to_cart(0).click()
        self.homepage.cart().click()
        self.assertEqual(self.cart.item_id_by_row(0), item_id1)
        self.assertEqual(self.cart.product_id_by_row(0), product_id1)
        self.assertEqual(self.cart.description_by_row(0), description1)
        self.assertEqual(self.cart.list_price_by_unit(0), unit_price1)
        self.assertEqual(self.cart.multiply_qty_by_list_price(0), self.cart.total_cost_by_row(0))
        self.homepage.Home_Page_Button().click()
        self.homepage.Cats_Picture().click()
        product_id2 = self.categories.product_id_seeker(0)
        self.categories.cat_items(0).click()
        item_id2 = self.categories.item_id_seeker(0)
        description2 = self.categories.item_description(0)
        unit_price2 = self.categories.list_price(0)
        self.categories.add_to_cart(0).click()
        self.homepage.cart().click()
        self.assertEqual(self.cart.item_id_by_row(1), item_id2)
        self.assertEqual(self.cart.product_id_by_row(1), product_id2)
        self.assertEqual(self.cart.description_by_row(1), description2)
        self.assertEqual(self.cart.list_price_by_unit(1), unit_price2)
        self.assertEqual(self.cart.multiply_qty_by_list_price(1), self.cart.total_cost_by_row(1))
        self.homepage.Home_Page_Button().click()
        self.homepage.Dogs_Top().click()
        product_id3 = self.categories.product_id_seeker(4)
        self.categories.dog_items(4).click()
        item_id3 = self.categories.item_id_seeker(3)
        description3 = self.categories.item_description(3)
        unit_price3 = self.categories.list_price(3)
        self.categories.add_to_cart(3).click()
        self.homepage.cart().click()
        self.assertEqual(self.cart.item_id_by_row(2), item_id3)
        self.assertEqual(self.cart.product_id_by_row(2), product_id3)
        self.assertEqual(self.cart.description_by_row(2), description3)
        self.assertEqual(self.cart.list_price_by_unit(2), unit_price3)
        self.assertEqual(self.cart.multiply_qty_by_list_price(2), self.cart.total_cost_by_row(2))
        self.assertEqual(self.cart.sub_total(), self.cart.global_qty_by_list_price(0,1,2))

    def test_3_task(self):
        '''Checking if the "remove" button works properly in the cart page'''
        self.homepage.Reptiles_Top().click()
        self.categories.reptile_items(0).click()
        self.categories.add_to_cart(0).click()
        self.homepage.Home_Page_Button().click()
        self.homepage.Cats_Left().click()
        self.categories.cat_items(0).click()
        description = self.categories.item_description(0)
        self.categories.add_to_cart(0).click()
        self.homepage.cart().click()
        self.cart.remove_item(1).click()
        self.assertNotIn(description, self.cart.global_descriptions())

    def test_4_task(self):
        '''Checking that the text "Shopping Cart" indeed shows in the cart page'''
        self.homepage.Reptiles_Top().click()
        self.categories.reptile_items(0).click()
        self.categories.add_to_cart(0).click()
        self.assertEqual(self.cart.shopping_cart_text(), 'Shopping Cart')

    def test_5_task(self):
        '''Add 3 items to the cart and assert that the subtotal is calculated correctly by calculating each
        item quantity and price and combining them, and printing every product description, quantity and total price.'''
        # =====================First Item=======================
        self.homepage.Reptiles_Top().click()
        self.categories.reptile_items(1).click()
        self.categories.add_to_cart(0).click()
        self.homepage.cart().click()
        self.homepage.Home_Page_Button().click()
        # =====================Second Item=======================
        self.homepage.Cats_Picture().click()
        self.categories.cat_items(0).click()
        self.categories.add_to_cart(0).click()
        self.homepage.cart().click()
        self.homepage.Home_Page_Button().click()
        # =====================Third Item=======================
        self.homepage.Dogs_Top().click()
        self.categories.dog_items(4).click()
        self.categories.add_to_cart(3).click()
        self.homepage.cart().click()
        self.cart.quantity_changer_flow(2, 55)
        self.cart.update_cart().click()
        self.assertEqual(self.cart.sub_total(), self.cart.global_qty_by_list_price(0, 1, 2))
        print(f"#1 Description:{self.cart.description_by_row(0)} | #1 Quantity:{self.cart.qty_per_row(0)} | #1 Total Price:{self.cart.total_cost_element(0)}\n")
        print(f"#2 Description:{self.cart.description_by_row(1)} | #2 Quantity:{self.cart.qty_per_row(1)} | #2 Total Price:{self.cart.total_cost_element(1)}\n")
        print(f"#3 Description:{self.cart.description_by_row(2)} | #3 Quantity:{self.cart.qty_per_row(2)} | #3 Total Price:{self.cart.total_cost_element(2)}\n")

    def test_6_task(self):
        '''assert that after hitting back, we go back to the correct pages'''
        self.homepage.Reptiles_Top().click()
        self.categories.reptile_items(1).click()
        self.driver.back()
        self.assertIn('categoryId=REPTILES', self.driver.current_url)
        self.driver.back()
        self.assertEqual(self.driver.current_url, 'https://petstore.octoperf.com/actions/Catalog.action')

    def test_7_task(self):
        '''Create a new account, perform a purchase and assert that the order number indeed shows in the order page,
        and it matches it.'''
        self.homepage.Birds_Left().click()
        self.categories.birds_items(0).click()
        self.categories.add_to_cart(0).click()
        self.homepage.cart().click()
        self.cart.proceed_to_checkout().click()
        self.login.create_new_user_button().click()
        self.acc.registration_flow('shisui2', '19287Yajh', '19287Yajh', 'might', 'guy', 'random@mail.com', '123456789',
                          'israel','random street 1/2', 'safed', 'hazafon', '12345', 'israel', 'english', 'CATS')
        self.homepage.cart().click()
        self.cart.proceed_to_checkout().click()
        self.checkout.payment_flow('American Express', '1234567812345678', '09/28')
        self.checkout.confirm().click()
        order_number = self.checkout.copy_order_number()
        self.assertEqual(self.checkout.checkout_successful_msg(), 'Thank you, your order has been submitted.')
        self.homepage.sign_in().click()
        self.login.sign_in_flow('shisui2', '19287Yajh')
        self.homepage.my_account().click()
        self.homepage.my_orders().click()
        self.assertEqual(self.homepage.order_number_by_row(-1), order_number)

    def test_8_task(self):
        '''Add 1 item to the cart, sign in using existing acc, pay with visa and check that the order is indeed in
        the my orders page, and the cart is empty after purchasing.'''
        self.homepage.Birds_Left().click()
        self.categories.birds_items(0).click()
        self.categories.add_to_cart(0).click()
        self.homepage.cart().click()
        self.cart.proceed_to_checkout().click()
        self.login.sign_in_flow('shisui2', '19287Yajh')
        self.homepage.cart().click()
        self.cart.proceed_to_checkout().click()
        self.checkout.payment_flow('Visa', '1234567812345678', '09/28')
        self.checkout.confirm().click()
        order_number = self.checkout.copy_order_number()
        self.homepage.my_account().click()
        self.homepage.my_orders().click()
        self.assertEqual(self.homepage.order_number_by_row(-1), order_number)
        self.homepage.cart().click()
        self.assertEqual(self.cart.cart_empty(), 'Your cart is empty.')

    def test_9_task(self):
        '''Assert we are indeed signed in, and assert we are signed out.'''
        self.homepage.sign_in().click()
        self.login.sign_in_flow('sasuke', '19287Yajh')
        self.homepage.my_account().click()
        self.assertEqual(self.homepage.account_user_id_text(), 'sasuke')
        self.homepage.sign_out().click()
        self.homepage.sign_in().click()
        self.assertEqual(self.homepage.sign_in_existing_header(), 'Please enter your username and password.')

    def tearDown(self):
        self.driver.quit()


