from Locators.Locators import LocatorsClass
from Common.CustomFind.FindElement import CustomFindElement


class CartClass():
    def __init__(self, driver):
        self.locators = LocatorsClass()
        self.driver = driver
        self.customFind = CustomFindElement(self.driver)


    def my_product_displayed(self):
        myProduct = self.customFind.find_element(self.locators.myProduct)
        try:
        #myProduct = self.driver.find_element(self.locators.myProduct[0], self.locators.myProduct[1])
            print (myProduct.is_displayed())
        except:
            print("The product has not been added to the card")

    def press_my_product_delete_button(self):
        try:
            for delete in self.driver.page_source:
                pressDeleteButton = self.customFind.find_element(self.locators.DeleteButton)
                pressDeleteButton.click()
        except:
            print("cart is empty")
