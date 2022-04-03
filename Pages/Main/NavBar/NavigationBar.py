import time
from Locators.Locators import LocatorsClass
from Common.CustomFind.FindElement import CustomFindElement
from selenium.webdriver import ActionChains
from Common.Variables.Variables import VariablesClass

class NavigationBarClass():
    def __init__(self, driver):
        self.locators = LocatorsClass()
        self.driver = driver
        self.customFind = CustomFindElement(self.driver)
        self.variables = VariablesClass()


    def fill_search_field(self,):
        searchfield = self.customFind.find_element(self.locators.navigationBarSearchFieldLocator)
        #searchfield = self.driver.find_element(self.locators.navigationBarSearchFieldLocator[0], self.locators.navigationBarSearchFieldLocator[1])
        searchfield.send_keys(self.variables.searchProduct)


    def press_into_search_button(self):
        searchbutton = self.customFind.find_element(self.locators.navigationBarSearchButtonLocator)
        #searchbutton = self.driver.find_element(self.locators.navigationBarSearchButtonLocator[0], self.locators.navigationBarSearchButtonLocator[1])
        searchbutton.click()


    def open_cart(self):
        cartButton = self.customFind.find_element(self.locators.cartButton)
        #cartButton = self.driver.find_element(self.locators.cartButton[0], self.locators.cartButton[1])
        cartButton.click()


    def account_and_lists(self):
        feelAccountAndLists = self.customFind.find_element(self.locators.accountAndLists)
        action = ActionChains(self.driver)
        action.move_to_element(feelAccountAndLists).perform()


    def recommendations_button(self):
        recommendationsButton = self.customFind.find_element(self.locators.Recommendations)
        recommendationsButton.click()

    def click_sign_out_button(self):
        clickSignOutButton = self.customFind.find_element(self.locators.signOutButton)
        clickSignOutButton.click()












