import time
from Locators.Locators import LocatorsClass
from Common.CustomFind.FindElement import CustomFindElement
from Common.Variables.Variables import VariablesClass

class PasswordClass():
    def __init__(self, driver):
        self.locators = LocatorsClass()
        self.driver = driver
        self.customFind = CustomFindElement(self.driver)
        self.variables = VariablesClass()


    def fill_password_field(self,):
        passwordField = self.customFind.find_element(self.locators.passwordPagePasswordFieldLocator)
        #passwordField = self.driver.find_element(self.locators.passwordPagePasswordFieldLocator[0], self.locators.passwordPagePasswordFieldLocator[1])
        passwordField.send_keys(self.variables.defoultPassword)
        time.sleep(4)


    def click_into_SignIn_button(self):
        signInButton = self.customFind.find_element(self.locators.passwordPageSignInButtonLocator)
        #signInButton = self.driver.find_element(self.locators.passwordPageSignInButtonLocator[0], self.locators.passwordPageSignInButtonLocator[1])
        signInButton.click()