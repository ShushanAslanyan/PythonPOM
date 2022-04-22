import time

from Pages.Common.BaseClass import BaseClass


class PasswordClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_password_field(self, ):
        passwordField = self.customFind.find_element(self.locators.passwordPagePasswordFieldLocator)
        passwordField.send_keys(self.variables.defoultPassword)
        time.sleep(4)

    def click_into_SignIn_button(self):
        signInButton = self.customFind.find_element(self.locators.passwordPageSignInButtonLocator)
        signInButton.click()
        time.sleep(5)
