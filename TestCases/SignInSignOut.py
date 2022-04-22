import unittest

from Pages.Common.BaseClassTestCases import BaseClassTestCasesClass


class SignInSignOut(unittest.TestCase, BaseClassTestCasesClass):
    def setUp(self):
        self.base()

    def test_signIn(self):
        self.driver.get(self.variables.amazonLink)
        self.loginPage.fill_login_field()
        self.loginPage.press_into_continue_button()
        self.passwordPage.fill_password_field()
        self.passwordPage.click_into_SignIn_button()

    def tearDown(self):
        self.navigationBar.account_and_lists()
        self.navigationBar.click_sign_out_button()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
