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

    def get_radio_button_selections(self):
        radio_buttons = self.driver.find_elements(By.XPATH, '//input[@type="radio"]')
        selections = {}

        for button in radio_buttons:
            button_id = button.get_attribute('id')
            is_selected = button.is_selected()
            selections[button_id] = is_selected

        return selections

    def check(self, button_name: str) -> None:
        root_loc = self.target_radio_button_xpath.format(button_name)
        label_loc = root_loc + '//label'
        input_loc = root_loc + '//input'
        label_el = self.driver.find_element(By.XPATH, label_loc)
        input_el = self.driver.find_element(By.XPATH, input_loc)
        if not input_el.is_selected():
            label_el.click()

    def check_if_radio_button_was_selected_by_name(self, button_name: str) -> bool:
        radio_xpath = "//span[@class='text-success'][contains(text(),'{0}')]".format(button_name)
        radio_button_result_message = self.driver.find_element(By.XPATH, radio_xpath)
        if radio_button_result_message.is_displayed():
            return True
        else:
            return False

    def check_disabled_radio_button(self) -> None:
        label = self.driver.find_element(By.CSS_SELECTOR, 'label.custom-control-label.disabled[for="noRadio"]')
        radio_button = self.driver.find_element(By.ID, 'noRadio')

        self.driver.execute_script("""
            arguments[0].classList.remove('disabled');
            arguments[1].removeAttribute('disabled');
            arguments[1].click();
            """, label, radio_button)

    def is_disabled_radio_button_was_selected(self) -> bool:
        radio_button = self.driver.find_element(By.ID, 'noRadio')
        return radio_button.is_selected()
