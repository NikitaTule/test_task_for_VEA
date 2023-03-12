from base.selenium_base import SeleniumBase


class AuthorizationPage:

    def __init__(self, driver, selenium=SeleniumBase):
        self.driver = driver
        self.selenium = selenium(driver)
        pass
