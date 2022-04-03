from selenium.webdriver.common.by import By


class LocatorsClass():
    # LoginPage Locators
    loginPageLoginFieldLocator = (By.ID, "ap_email")
    loginPageContinueButtonLocator = (By.ID, "continue")

    # PasswordPage Locators
    passwordPagePasswordFieldLocator = (By.ID, "ap_password")
    passwordPageSignInButtonLocator = (By.ID, "signInSubmit")

    # searchfield Locators
    navigationBarSearchFieldLocator = (By.ID, "twotabsearchtextbox")
    navigationBarSearchButtonLocator = (By.ID, "nav-search-submit-button")

    # select Product Locator
    selectProductClick = (By.XPATH, "(//img[@class='s-image'])[1]")

    # Add to Cart Button Locator
    addToCartButton = (By.ID, "add-to-cart-button")

    # Open Cart Button Locator
    cartButton = (By.ID, "nav-cart-count")

    # My Product displayed
    myProduct = (By.XPATH, "//div[@class='a-row a-spacing-base a-spacing-top-base'][1]")

    # My Product Delete Button
    DeleteButton = (By.XPATH, "//input[@value='Delete']")

    # Account & Lists
    accountAndLists = (By.ID, "nav-link-accountList")

    # Recommendations Button
    Recommendations = (By.LINK_TEXT, "Recommendations")

    # Recommendation Third Product
    recommendationThirdProduct = (By.ID, "p13n-asin-index-2")




    # Add To Cart By name
    #addToCartByName = (By.NAME, "submit.addToCart")

    # Open Third Product
    openThirdProduct = (By. XPATH, "//div[@class='a-cardui _cDEzb_gridExpansion_vuxFX p13n-grid-detail']")
    #// div[ @ id = 'expansion-2'] / div / div / div[2] / div[2] / div[1] / a / span

    # Sign Out Button
    signOutButton = (By.LINK_TEXT, "Sign Out")



