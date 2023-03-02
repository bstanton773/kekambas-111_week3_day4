from whiteboard import solution
from unittest import TestCase


class TestCheckDouble(TestCase):

    def test_empty_list(self):
        result = solution([])
        self.assertFalse(result)

    def test_one_double(self):
        result = solution([2, 4, 6])
        self.assertTrue(result)

    def test_multiple_doubles(self):
        result = solution([10, 2, 5, 3])
        self.assertTrue(result)

    def test_odd_numbers(self):
        result = solution([7, 1, 14, 11])
        self.assertTrue(result)

    def test_no_double_odd_numbers(self):
        result = solution([3, 1, 7, 11])
        self.assertFalse(result)
