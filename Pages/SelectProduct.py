from Locators.Locators import LocatorsClass
from Common.CustomFind.FindElement import CustomFindElement

class SelectProductClass():
    def __init__(self, driver):
        self.locators = LocatorsClass()
        self.driver = driver
        self.customFind = CustomFindElement(self.driver)


    def select_the_product(self):
        selectProduct = self.customFind.find_element(self.locators.selectProductClick)
        #selectProduct = self.driver.find_element(self.locators.selectProductClick[0], self.locators.selectProductClick[1])
        selectProduct.click()


    def press_add_to_cart_button(self):
        try:
            addToCart = self.customFind.find_element(self.locators.addToCartButton)
            addToCart.click()
        except:
            print("The product cannot be added to the cart")