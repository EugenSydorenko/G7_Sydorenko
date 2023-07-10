from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class PageDynamicProperties:
    URL = 'https://demoqa.com/dynamic-properties'

    def __init__(self, driver: WebDriver):

        self.driver = driver
        self.dynamic_id_element_loc = (By.XPATH, '//div/p[text()][not(contains(@id, "error"))][not(@jsselect)]')
        self.enable_disable_button_loc = By.CSS_SELECTOR, '#enableAfter'
        self.change_color_button_loc = By.CSS_SELECTOR, '[id="colorChange"]'
        self.appeared_button_loc = By.CSS_SELECTOR, '#visibleAfter'
        self.text_locator = By.XPATH, "//p[text()='This text has random Id']"

    def open(self) -> 'PageDynamicProperties':
        self.driver.get(self.URL)
        return self

    def get_dynamic_id_element_attrib(self, attribute: str) -> str:
        element = self.driver.find_element(*self.dynamic_id_element_loc)
        return element.get_attribute(attribute)

    def button_enabled_disabled(self) -> WebElement:
        button = self.driver.find_element(*self.enable_disable_button_loc)
        self.wait(6).until(ec.element_to_be_clickable(button))
        return button

    @staticmethod
    def attribute_value_to_include(element: WebElement, attribute_name, attribute_value) -> bool:
        return attribute_value in element.get_attribute(attribute_name)

    def button_change_color(self) -> WebElement:
        button = self.driver.find_element(*self.change_color_button_loc)
        self.wait(10).until(lambda driver: self.attribute_value_to_include(button, 'class', 'text-danger'))
        return button

    def button_appeared(self) -> WebElement:
        return WebDriverWait(self.driver, timeout=6).until(
            ec.visibility_of_element_located(self.appeared_button_loc))

    def wait(self, seconds: int) -> WebDriverWait:
        return WebDriverWait(self.driver, seconds)

    def text_with_dynamic_id(self) -> WebElement:
        text_element = self.driver.find_element(*self.text_locator)
        return text_element
