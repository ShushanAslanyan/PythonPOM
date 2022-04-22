from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CustomFindElement():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element
        except:
            print("Locator is not found as")
