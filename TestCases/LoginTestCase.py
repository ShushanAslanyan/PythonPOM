import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Common.Variables.Variables import VariablesClass
from Pages.CartPage import CartClass
from Pages.LoginPage import LoginClass
from Pages.Main.NavBar.NavigationBar import NavigationBarClass
from Pages.PasswordPage import PasswordClass
from Pages.RecommendationPage import RecommendationClass
from Pages.SelectProduct import SelectProductClass


class LogIn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variables = VariablesClass()
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)
        cls.loginPage = LoginClass(cls.driver)
        cls.passwordPage = PasswordClass(cls.driver)
        cls.navigationBar = NavigationBarClass(cls.driver)
        cls.selectProduct = SelectProductClass(cls.driver)
        cls.cartPage = CartClass(cls.driver)
        cls.recommendationPage = RecommendationClass(cls.driver)

    def test_PositiveLogIn(self):
        self.driver.get(self.variables.amazonLink)
        self.loginPage.fill_login_field()
        self.loginPage.press_into_continue_button()
        self.passwordPage.fill_password_field()
        self.passwordPage.click_into_SignIn_button()
        self.navigationBar.fill_search_field()
        self.navigationBar.press_into_search_button()
        self.selectProduct.get_item_attribute()
        self.selectProduct.select_the_product()
        self.selectProduct.press_add_to_cart_button()
        self.navigationBar.open_cart()
        self.cartPage.check_item_in_cart(self.selectProduct.getItemAttribute)
        self.cartPage.delete_all_products_from_cart()
        self.navigationBar.account_and_lists()
        self.navigationBar.recommendations_button()
        self.recommendationPage.select_third_product()
        self.recommendationPage.open_third_product()
        self.selectProduct.press_add_to_cart_button()

    def tearDown(self):
        self.navigationBar.account_and_lists()
        self.navigationBar.click_sign_out_button()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
