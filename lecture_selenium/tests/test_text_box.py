from lecture_selenium.pages.page_text_box import PageTextBox

user_data = {'fullname': 'Vasya Pupkin',
             'email': 'pupkin@1.com',
             'curr_addr': 'My current address',
             'perm_addr': 'My perm address'}


class TestTextBox:

    def test_full_name(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_full_name(user_data.get('fullname'))
        page.submit()
        name = page.get_full_name()
        assert name == user_data['fullname']

    def test_email_positive(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_email(user_data.get('email'))
        page.submit()
        email = page.get_email()
        assert email == user_data['email']

    def test_email_negative(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_email('@' + user_data.get('email'))
        page.submit()
        email_field_attribute = page.get_email_field_attribute('class')
        assert 'field-error' in email_field_attribute

    def test_curr_addr(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_curr_addr(user_data.get('curr_addr'))
        page.submit()
        curr_addr = page.get_curr_addr()
        assert curr_addr == user_data['curr_addr']

    def test_perm_addr(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_perm_addr(user_data.get('perm_addr'))
        page.submit()
        perm_addr = page.get_perm_addr()
        assert perm_addr == user_data['perm_addr']

    def test_full_form_positive(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_full_name(user_data.get('fullname')).set_email(user_data.get('email')).set_curr_addr(
            user_data.get('curr_addr')).set_perm_addr(user_data.get('perm_addr')).submit()
        actual_user_data = {'fullname': page.get_full_name(), 'email': page.get_email(),
                            'curr_addr': page.get_curr_addr(), 'perm_addr': page.get_perm_addr()}

        assert actual_user_data == user_data

    def test_full_form_negative(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_full_name(user_data.get('fullname')).set_email('@' + user_data.get('email')).set_curr_addr(
            user_data.get('curr_addr')).set_perm_addr(user_data.get('perm_addr')).submit()
        email_field_attribute = page.get_email_field_attribute('class')

        assert page.check_if_output_test_areas_exist() == False and 'field-error' in email_field_attribute
