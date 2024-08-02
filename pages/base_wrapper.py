from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseWrapper:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.default_timer = 15

    def find_element(self, locator: tuple[By, str], timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator),
            message=f'Элемент {locator} не найден')

    def find_elements(self, locator: tuple[By, str], timeout: int = 10) -> list[WebElement]:
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_all_elements_located(locator),
            message=f'Элементы {locator} не найдены')

    def find_dynamic_element(self, locator: tuple[By, str], *parameters) -> WebElement:
        return self.find_element(self.format_dynamic_locator(locator, *parameters))

    @staticmethod
    def format_dynamic_locator(dynamic_locator: tuple[By, str], *parameters) -> tuple[By, str]:
        return dynamic_locator[0], dynamic_locator[1].format(*parameters)

    def clear_and_send_keys(self, locator: tuple[By, str], value: (int, str)) -> None:
        """Метод очищает поле и вносит в него новое значение"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)

    def is_element_visible(self, locator: tuple[By, str]) -> bool:
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False
