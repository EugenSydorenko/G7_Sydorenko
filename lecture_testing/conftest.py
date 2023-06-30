import pytest


@pytest.fixture(scope='function')
def my_first_fixture_placed_in_package():
    print('\nSetup before each test')
    yield
    print('\nTearDown after each test')


@pytest.fixture(scope='class')
def class_fixture():
    print('\nSetup before class')
    yield ['my', 'class', 'fixture', 'text', 'dog']
    print('\nTearDown after class')
