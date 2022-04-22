import time

from selenium.webdriver import ActionChains

from Pages.Common.BaseClass import BaseClass


class NavigationBarClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_search_field(self, ):
        searchfield = self.customFind.find_element(self.locators.navigationBarSearchFieldLocator)
        searchfield.send_keys(self.variables.searchProduct)

    def press_into_search_button(self):
        searchbutton = self.customFind.find_element(self.locators.navigationBarSearchButtonLocator)
        searchbutton.click()

    def open_cart(self):
        cartButton = self.customFind.find_element(self.locators.cartButton)
        cartButton.click()

    def account_and_lists(self):
        feelAccountAndLists = self.customFind.find_element(self.locators.accountAndLists)
        action = ActionChains(self.driver)
        action.move_to_element(feelAccountAndLists).perform()

    def recommendations_button(self):
        recommendationsButton = self.customFind.find_element(self.locators.Recommendations)
        recommendationsButton.click()
        time.sleep(2)

    def click_sign_out_button(self):
        clickSignOutButton = self.customFind.find_element(self.locators.signOutButton)
        clickSignOutButton.click()
