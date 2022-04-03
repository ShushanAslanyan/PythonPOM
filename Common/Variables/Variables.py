import os
from pathlib import Path

class VariablesClass():
    defoultLogin = "shushanAsl@yahoo.com"
    defoultPassword = "QATest@2022"
    searchProduct = "3d pen"
    amazonLink = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"

    def generatePath(self):
        ROOT_DIR = Path(__file__).absolute().parent.parent.parent
        PATH = str(ROOT_DIR)+"\Common\Driver\chromedriver.exe"
        PATH = PATH.replace("\\","\\\\")
        return PATH




'''
if __name__ == "__main__":
    obj = VariablesClass()
    #print(obj.getPrjRoot())
    #print(obj.generatePath())
'''