import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from lecture_selenium.pages.page_alerts import PageAlerts


@pytest.mark.usefixtures('chrome')
class TestAlerts:

    def test_just_alert(self):
        page = PageAlerts(self.driver).open()
        alert = page.get_just_alert()
        assert alert.text == 'You clicked a button'
        alert.accept()

    def test_timed_alert(self):
        page = PageAlerts(self.driver).open()
        page.get_timed_alert()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(ec.alert_is_present())
        assert alert.text == 'This alert appeared after 5 seconds'
        alert.accept()

    def test_confirm_box(self):
        page = PageAlerts(self.driver).open()

        alert = page.get_confirm_box()
        alert.accept()
        assert 'Ok' in page.get_confirm_box_result()

        alert = page.get_confirm_box()
        alert.dismiss()
        assert 'Cancel' in page.get_confirm_box_result()

    def test_prompt_box(self):
        text = 'text to prompt box'
        page = PageAlerts(self.driver).open()
        alert = page.get_prompt_box()
        alert.send_keys(text)
        time.sleep(3)
        alert.accept()
        assert text in page.get_prompt_box_result()
        print(page.get_prompt_box_result())
