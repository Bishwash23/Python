import unittest
from main import find_largest

class TestFindLargest(unittest.TestCase):

    def test_positive_numbers(self):
        result = find_largest([3, 8, 2, 10, 5])
        self.assertEqual(result, 10, "The largest element is incorrect for the list [3, 8, 2, 10, 5]")

    def test_negative_numbers(self):
        result = find_largest([-5, -10, -2, -1, -7])
        self.assertEqual(result, -1, "The largest element is incorrect for the list [-5, -10, -2, -1, -7]")

    def test_mixed_numbers(self):
        result = find_largest([-3, 0, 5, -10, 8, 2])
        self.assertEqual(result, 8, "The largest element is incorrect for the list [-3, 0, 5, -10, 8, 2]")

    def test_single_element(self):
        result = find_largest([42])
        self.assertEqual(result, 42, "The largest element is incorrect for a single-element list [42]")

    def test_duplicate_largest(self):
        result = find_largest([5, 5, 3, 5, 4])
        self.assertEqual(result, 5, "The largest element is incorrect for the list with duplicate largest [5, 5, 3, 5, 4]")

if __name__ == '__main__':
    unittest.main()