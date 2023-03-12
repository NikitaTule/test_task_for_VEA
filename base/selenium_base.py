from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumBase:
    """ Методы для поиска, ожидания появления, исчезновения вебэлментов """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 6)
        self.driver.set_script_timeout(5)

    def is_visible(self, locator: str, message: str = "") -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator),
                               message=f"Элемент не найден=> {locator}" or message)

    def is_present(self, locator: str, message: str = "") -> WebElement:
        return self.wait.until(ec.presence_of_element_located(locator),
                               message=f"Элемент не найден=> {locator}" or message)

    def is_clickable(self, locator: str, message: str = "") -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator),
                               message=f"Элемент не найден=> {locator}" or message)

    def are_visible(self, locator: str, message: str = "") -> list[WebElement]:
        return self.wait.until(ec.visibility_of_any_elements_located(locator),
                               message=f"Элементs не найдены=> {locator}" or message)

    def text_present_in_element(self, locator: str, text: str, message: str = "") -> WebElement:
        return self.wait.until(ec.text_to_be_present_in_element(locator, text),
                               message=f"Элемент не найден=> {locator}" or message)

    def dont_visible(self, locator: str, message: str = "") -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located(locator),
                               message=f"Элемент не исчез=> {locator}" or message)
