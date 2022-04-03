import time
import unittest
from selenium import webdriver
from Pages.LoginPage import LoginClass
from Pages.PasswordPage import PasswordClass
from Common.Variables.Variables import VariablesClass
from Pages.Main.NavBar.NavigationBar import NavigationBarClass
from Pages.SelectProduct import SelectProductClass
from Pages.CartPage import CartClass
from Pages.RecommendationPage import RecommendationClass


class LogIn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variables = VariablesClass()
        #cls.driver = webdriver.Chrome("..\\Common\\Driver\\chromedriver.exe")
        #print(cls.variables.generatePath())
        cls.driver = webdriver.Chrome(cls.variables.generatePath())
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)
        cls.loginPage = LoginClass(cls.driver)
        cls.passwordPage = PasswordClass(cls.driver)
        cls.navigationBar = NavigationBarClass(cls.driver)
        cls.selectProduct = SelectProductClass(cls.driver)
        cls.cartPage = CartClass(cls.driver)
        cls.recommendationPage = RecommendationClass(cls.driver)

    def setUp(self):
        pass


    def test_PositiveLogIn(self):
        self.driver.get(self.variables.amazonLink)
        self.loginPage.fill_login_field()
        self.loginPage.press_into_continue_button()
        self.passwordPage.fill_password_field()
        self.passwordPage.click_into_SignIn_button()
        time.sleep(5)
        self.navigationBar.fill_search_field()
        self.navigationBar.press_into_search_button()
        self.selectProduct.select_the_product()
        self.selectProduct.press_add_to_cart_button()
        self.navigationBar.open_cart()
        self.cartPage.my_product_displayed()
        self.cartPage.press_my_product_delete_button()
        self.navigationBar.account_and_lists()
        self.navigationBar.recommendations_button()
        time.sleep(2)
        self.recommendationPage.select_third_product()
        time.sleep(2)
        self.recommendationPage.open_third_product()
        self.selectProduct.press_add_to_cart_button()
        #self.recommendationPage.add_to_cart_by_name()
        time.sleep(5)


    def tearDown(self):
        self.navigationBar.account_and_lists()
        self.navigationBar.click_sign_out_button()
        self.driver.close()



if __name__ == '__main__':
    unittest.main()