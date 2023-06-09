import pytest

from lecture_selenium.pages.page_dynamic_properties import PageDynamicProperties


@pytest.mark.usefixtures('chrome')
class TestDynamicProperties:

    def test_is_button_appears(self):
        page = PageDynamicProperties(self.driver).open()
        button = page.button_appeared()
        assert button.is_displayed()

    def test_is_button_enabled(self):
        page = PageDynamicProperties(self.driver).open()
        button = page.button_enabled_disabled()
        assert button.is_enabled()

    def test_is_button_color_changed(self):
        page = PageDynamicProperties(self.driver).open()
        button = page.button_change_color()
        class_attribute = button.get_attribute('class')
        assert 'text-danger' in class_attribute

    def test_get_dynamic_text_id(self):
        page = PageDynamicProperties(self.driver).open()
        print('\nNew text id = ', page.text_with_dynamic_id().get_attribute('id'))
        pass
