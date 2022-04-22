from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Common.Variables.Variables import VariablesClass
from Pages.LoginPage import LoginClass
from Pages.Main.NavBar.NavigationBar import NavigationBarClass
from Pages.PasswordPage import PasswordClass


class BaseClassTestCasesClass():
    def base(self):
        self.variables = VariablesClass()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.loginPage = LoginClass(self.driver)
        self.passwordPage = PasswordClass(self.driver)
        self.navigationBar = NavigationBarClass(self.driver)
