import unittest

from Pages.Common.BaseClassTestCases import BaseClassTestCasesClass
from Pages.SelectProduct import SelectProductClass


class AddProduct(unittest.TestCase, BaseClassTestCasesClass):
    def setUp(self):
        self.base()
        self.selectProduct = SelectProductClass(self.driver)

    def test_selectAndAddProduct(self):
        self.driver.get(self.variables.amazonLink)
        self.loginPage.fill_login_field()
        self.loginPage.press_into_continue_button()
        self.passwordPage.fill_password_field()
        self.passwordPage.click_into_SignIn_button()
        self.navigationBar.fill_search_field()
        self.navigationBar.press_into_search_button()
        self.selectProduct.select_the_product()
        self.selectProduct.press_add_to_cart_button()

    def tearDown(self):
        self.navigationBar.account_and_lists()
        self.navigationBar.click_sign_out_button()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
