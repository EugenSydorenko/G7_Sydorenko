import pytest

from lecture_selenium.pages.page_radio_button import PageRadioButton


@pytest.mark.usefixtures('chrome')
class TestRadioButton:

    def test_radio_button(self):
        page = PageRadioButton(self.driver)
        page.open()
        assert len(page.get_all_possible_radio_buttons()) == 3

    def test_select_button(self):
        button_name = 'Impressive'
        page = PageRadioButton(self.driver)
        page.open()
        page.check(button_name)
        pass

    def test_select_button(self):
        button_name = 'Impressive'
        page = PageRadioButton(self.driver)
        page.open()
        page.check(button_name)
        pass

