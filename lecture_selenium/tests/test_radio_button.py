import pytest

from lecture_selenium.pages.page_radio_button import PageRadioButton


@pytest.mark.usefixtures('chrome')
class TestRadioButton:

    def test_radio_button(self):
        page = PageRadioButton(self.driver)
        page.open()
        assert len(page.get_all_possible_radio_buttons()) == 3

    def test_select_button(self):
        button_name = 'Yes'
        page = PageRadioButton(self.driver)
        page.open()
        page.check(button_name)
        assert page.check_if_radio_button_was_selected_by_name(button_name)

    def test_select_disabled_radio(self):
        page = PageRadioButton(self.driver)
        page.open()
        page.check_disabled_radio_button()
        assert page.is_disabled_radio_button_was_selected()

    def test_show_all_radio_buttons(self):
        page = PageRadioButton(self.driver)
        page.open()
        print(page.get_radio_button_selections())
        pass
