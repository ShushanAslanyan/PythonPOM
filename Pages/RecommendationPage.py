import time

from Pages.Common.BaseClass import BaseClass


class RecommendationClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def select_third_product(self):
        selectThirdProduct = self.customFind.find_element(self.locators.recommendationThirdProduct)
        selectThirdProduct.click()
        time.sleep(2)

    def open_third_product(self):
        openAndClick = self.customFind.find_element(self.locators.openThirdProduct)
        openAndClick.click()
