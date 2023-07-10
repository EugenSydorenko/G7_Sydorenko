from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageAlerts:
    URL = 'https://demoqa.com/alerts'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.just_alert_loc = By.ID, 'alertButton'
        self.timed_alert_loc = By.ID, 'timerAlertButton'
        self.confirm_box_loc = By.ID, 'confirmButton'
        self.prompt_box_loc = By.ID, 'promtButton'
        self.prompt_result_loc = By.ID, 'promptResult'
        self.confirm_result_loc = By.ID, 'confirmResult'

    def open(self) -> 'PageAlerts':
        self.driver.get(self.URL)
        return self

    def get_just_alert(self) -> Alert:
        element = self.driver.find_element(*self.just_alert_loc)
        element.click()
        return Alert(self.driver)

    def get_timed_alert(self):
        element = self.driver.find_element(*self.timed_alert_loc)
        element.click()
        return Alert(self.driver)

    def get_confirm_box(self):
        element = self.driver.find_element(*self.confirm_box_loc)
        element.click()
        return Alert(self.driver)

    def get_prompt_box(self):
        element = self.driver.find_element(*self.prompt_box_loc)
        element.click()
        return Alert(self.driver)

    def get_prompt_box_result(self):
        return self.driver.find_element(*self.prompt_result_loc).text

    def get_confirm_box_result(self):
        return self.driver.find_element(*self.confirm_result_loc).text
