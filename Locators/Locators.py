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
    selectProductClick = (
        By.XPATH, "(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[1]")

    # Add to Cart Button Locator
    addToCartButton = (By.ID, "add-to-cart-button")

    # Open Cart Button Locator
    cartButton = (By.ID, "nav-cart-count")

    # Cart Items Count
    cartItemsCountNumber = (By.ID, "nav-cart-count")

    # My Product Delete Button
    deleteButton = (By.XPATH, "//input[@value='Delete']")

    # Account & Lists
    accountAndLists = (By.ID, "nav-link-accountList")

    # Recommendations Button
    Recommendations = (By.LINK_TEXT, "Recommendations")

    # Recommendation Third Product
    recommendationThirdProduct = (By.ID, "p13n-asin-index-2")

    # Open Third Product
    openThirdProduct = (
        By.XPATH, "//div[@class='a-column a-span12 a-text-center _cDEzb_grid-detail-column_S6U61 expandedGridView']")

    # Sign Out Button
    signOutButton = (By.LINK_TEXT, "Sign Out")
