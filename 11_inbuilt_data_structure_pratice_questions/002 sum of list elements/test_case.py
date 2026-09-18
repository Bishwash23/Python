import unittest
from main import sum_list

class TestSumList(unittest.TestCase):

    def test_positive_numbers(self):
        result = sum_list([1, 2, 3, 4, 5])
        self.assertEqual(result, 15, "The sum is incorrect for the list [1, 2, 3, 4, 5]")

    def test_mixed_numbers(self):
        result = sum_list([10, -5, 7, 8, -2])
        self.assertEqual(result, 18, "The sum is incorrect for the list [10, -5, 7, 8, -2]")

    def test_empty_list(self):
        result = sum_list([])
        self.assertEqual(result, 0, "The sum should be 0 for an empty list")

    def test_single_element(self):
        result = sum_list([42])
        self.assertEqual(result, 42, "The sum is incorrect for a single-element list [42]")

if __name__ == '__main__':
    unittest.main()