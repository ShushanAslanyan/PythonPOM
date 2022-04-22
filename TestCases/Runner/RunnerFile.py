import unittest

from TestCases.AddProduct import AddProduct
from TestCases.DeleteAllItems import DeleteAllItems
from TestCases.SignInSignOut import SignInSignOut


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SignInSignOut("test_signIn"))
    suite.addTest(DeleteAllItems("test_delet"))
    suite.addTest(AddProduct("test_selectAndAddProduct"))
    return suite


if __name__ == "__main__":
    ranner = unittest.TextTestRunner()
    ranner.run(suite())
