import pytest
import logging

x = 4


@pytest.mark.skip(reason='Just skip')
def test_equals():
    assert x == 4


@pytest.mark.skipif(True, reason='x should be less than 5 to run test')
def test_skip_if():
    pass


@pytest.mark.smoke
def test_mark_smoke_1():
    print('smoke test 1')


@pytest.mark.smoke
def test_mark_smoke_2():
    print('smoke test 2')


@pytest.mark.guest
@pytest.mark.user
def test_double_marks_1():
    pass


@pytest.mark.user
def test_mark_user():
    pass


def test_clean_1():
    pass


class TestFixtures:

    # def test_in_class_1(self, my_first_fixture_placed_in_package):
    #     print('test_clean_2 does something')
    #     pass
    #
    # def test_in_class_2(self, my_first_fixture_placed_in_package):
    #     print('test_clean_2 does something')
    #     pass

    def test_in_class_1(self, class_fixture):
        assert 'dog' in class_fixture
        pass

    def test_in_class_2(self, class_fixture):
        logging.debug('test_clean_2 does something')
        print('\ntest_clean_2 does something')
        pass
