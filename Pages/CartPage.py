from Pages.Common.BaseClass import BaseClass
from Pages.SelectProduct import SelectProductClass


class CartClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.attribute = None
        self.selectProduct = SelectProductClass

    def check_item_in_cart(self, attribute):
        self.attribute = attribute
        if self.driver.page_source.find(self.attribute) != -1:
            print("Element in cart")
        else:
            print("No such element in cart")

    def delete_cart_first_item(self):
        pressDeleteButton = self.customFind.find_element(self.locators.deleteButton)
        if pressDeleteButton is not None:
            pressDeleteButton.click()

    def delete_all_products_from_cart(self):
        cartElementCount = self.customFind.find_element(self.locators.cartItemsCountNumber).text
        cartElementCount = int(cartElementCount)

        while cartElementCount > 0:
            self.delete_cart_first_item()
            cartElementCount -= 1
        if cartElementCount == 0:
            print("Cart is empty")
