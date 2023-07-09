from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageRadioButton:
    URL = 'https://demoqa.com/radio-button'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.radio_button_loc = (By.XPATH, '//div[contains(@class, "custom-radio")]')
        self.target_radio_button_xpath = '//div[contains(@class, "custom-radio")][.="{}"]'

    def open(self) -> None:
        self.driver.get(self.URL)

    def get_all_possible_radio_buttons(self) -> list:
        button_elements = self.driver.find_elements(*self.radio_button_loc)
        return [el.text for el in button_elements]

    def check(self, button_name: str) -> None:
        root_loc = self.target_radio_button_xpath.format(button_name)
        label_loc = root_loc + '//label'
        input_loc = root_loc + '//input'
        label_el = self.driver.find_element(By.XPATH, label_loc)
        input_el = self.driver.find_element(By.XPATH, input_loc)
        if not input_el.is_selected():
            label_el.click()
