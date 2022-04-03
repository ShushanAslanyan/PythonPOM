import time
from Pages.Common.BaseClass import BaseClass

class LoginClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_login_field(self):
        loginField = self.customFind.find_element(self.locators.loginPageLoginFieldLocator)
        loginField.send_keys(self.variables.defoultLogin)
        time.sleep(4)


    def press_into_continue_button(self):
        continueButton = self.customFind.find_element(self.locators.loginPageContinueButtonLocator)
        #continueButton = self.driver.find_element(self.locators.loginPageContinueButtonLocator[0], self.locators.loginPageContinueButtonLocator[1])
        continueButton.click()