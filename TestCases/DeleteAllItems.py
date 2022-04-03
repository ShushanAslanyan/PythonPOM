import time
import unittest
from selenium import webdriver
from Pages.LoginPage import LoginClass
from Pages.PasswordPage import PasswordClass
from Common.Variables.Variables import VariablesClass
from Pages.Main.NavBar.NavigationBar import NavigationBarClass
from Pages.CartPage import CartClass



class LogIn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variables = VariablesClass()
        cls.driver = webdriver.Chrome(cls.variables.generatePath())
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)
        cls.loginPage = LoginClass(cls.driver)
        cls.passwordPage = PasswordClass(cls.driver)
        cls.navigationBar = NavigationBarClass(cls.driver)
        cls.cartPage = CartClass(cls.driver)


    def test_PositiveLogIn(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.loginPage.fill_login_field()
        self.loginPage.press_into_continue_button()
        self.passwordPage.fill_password_field()
        self.passwordPage.click_into_SignIn_button()
        time.sleep(5)
        self.navigationBar.open_cart()
        self.cartPage.press_my_product_delete_button()

    def tearDown(self):
        self.navigationBar.account_and_lists()
        self.navigationBar.click_sign_out_button()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()