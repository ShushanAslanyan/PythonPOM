from Pages.Common.BaseClass import BaseClass


class SelectProductClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.getItemAttribute = "itemAttribute"

    def select_the_product(self):
        selectProduct = self.customFind.find_element(self.locators.selectProductClick)
        selectProduct.click()

    def get_item_attribute(self):
        self.getItemAttribute = \
            self.customFind.find_element(self.locators.selectProductClick).find_elements_by_tag_name("span")[
                0].get_attribute('innerHTML')
        print(str(self.getItemAttribute))
        return self.getItemAttribute

    def press_add_to_cart_button(self):
        try:
            addToCart = self.customFind.find_element(self.locators.addToCartButton)
            addToCart.click()
        except:
            print("The product cannot be added to the cart")
