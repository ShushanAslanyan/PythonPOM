from Locators.Locators import LocatorsClass
from Common.CustomFind.FindElement import CustomFindElement
from selenium.webdriver.common.by import By


class RecommendationClass():
    def __init__(self, driver):
        self.locators = LocatorsClass()
        self.driver = driver
        self.customFind = CustomFindElement(self.driver)


    def select_third_product(self):
        selectThirdProduct = self.customFind.find_element(self.locators.recommendationThirdProduct)
        selectThirdProduct.click()

    def open_third_product(self):
        openAndClick = self.customFind.find_element(self.locators.openThirdProduct)
        openAndClick.click()






'''
    def get_item_attribute(self):
        self.getItemAttribute = self.customFind.find_element(self.locators.porc).get_attribute("alt")
        print(str(self.getItemAttribute))
        return self.getItemAttribute
    
    def  click_get_item(self):
        clickGetItem = self.driver.find_element(By.LINK_TEXT, str(self.getItemAttribute))
        clickGetItem.click()
        

    def add_to_cart_by_name(self):
        try:
            addToCartRecomendationProduct = self.customFind.find_element(self.locators.addToCartByName)
            addToCartRecomendationProduct.click()
        except:
            print("The product cannot be added to the cart")

'''


'''
    def click_third_product(self):
        openThirdProduct = self.customFind.find_element(self.locators.clickThirdProduct)
        openThirdProduct.click()

'''




