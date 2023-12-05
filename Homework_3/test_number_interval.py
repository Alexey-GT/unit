import unittest

from number_interval import number_interval


class NumberInInterval(unittest.TestCase):
    def test_in_interval(self):
        self.assertTrue(number_interval(26))

    def test_is_not_interval(self):
        self.assertFalse(number_interval(24))

    def test_is_num_more_than_interval(self):
        self.assertFalse(number_interval(101))
