import unittest

from Pages.CartPage import CartClass
from Pages.Common.BaseClassTestCases import BaseClassTestCasesClass


class DeleteAllItems(unittest.TestCase, BaseClassTestCasesClass):
    def setUp(self):
        self.base()
        self.cartPage = CartClass(self.driver)

    def test_delet(self):
        self.driver.get(self.variables.amazonLink)
        self.loginPage.fill_login_field()
        self.loginPage.press_into_continue_button()
        self.passwordPage.fill_password_field()
        self.passwordPage.click_into_SignIn_button()
        self.navigationBar.open_cart()
        self.cartPage.delete_all_products_from_cart()

    def tearDown(self):
        self.navigationBar.account_and_lists()
        self.navigationBar.click_sign_out_button()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
