from Common.CustomFind.FindElement import CustomFindElement
from Common.Variables.Variables import VariablesClass
from Locators.Locators import LocatorsClass


class BaseClass():
    def __init__(self, driver):
        self.locators = LocatorsClass()
        self.driver = driver
        self.customFind = CustomFindElement(self.driver)
        self.variables = VariablesClass()
