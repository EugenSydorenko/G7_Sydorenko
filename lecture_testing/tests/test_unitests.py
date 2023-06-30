import unittest
from datetime import datetime
from unittest import TestCase


class BaseTest(TestCase):
    """Базовий тестовий клас для наслідування"""

    is_user_registered = False

    @classmethod
    def setUpClass(cls) -> None:
        """Хук, що запускає певні інструкції при ініціалізації класу"""
        print('\nInitializing class level parameters')
        cls.is_user_registered = True

    @classmethod
    def tearDownClass(cls) -> None:
        """Хук, що запускає певні інструкції при видаленні класу"""
        print('\nCleanup once after class')


class TestDates(BaseTest):
    """Базовий клас для тестів, пов'язаних з датами"""

    def setUp(self) -> None:
        """Хук, що запускає певні інструкції при ініціалізації тестового методу"""
        print('\nInitializing test level parameters')
        self.now = datetime.now()

    def tearDown(self) -> None:
        """Хук, що запускає певні інструкції при завершенні тестового методу"""
        del self.now
        print('\nCleanup after each test')


class TestToday(TestDates):
    def test_is_2023(self):
        self.assertEqual(self.now.year, 2023, 'Year not verified')
        print('Year is verified')

    def test_is_not_winter(self):
        self.assertNotIn(self.now.month, (11, 12, 1), 'Season not verified')
        print('Season is verified')


if __name__ == '__main___':
    unittest.main()
