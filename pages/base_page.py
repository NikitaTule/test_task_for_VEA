from base.selenium_base import SeleniumBase


class BasePage:

    def __init__(self, driver, selenium=SeleniumBase):
        self.driver = driver
        self.selenium = selenium(driver)

    def open_site(self, base_url: str):
        self.driver.get(base_url)
