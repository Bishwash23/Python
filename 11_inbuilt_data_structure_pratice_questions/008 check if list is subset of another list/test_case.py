import unittest
from main import is_subset

class TestIsSubset(unittest.TestCase):

    def test_example_case1(self):
        result = is_subset([1, 2, 3], [1, 2, 3, 4, 5])
        self.assertTrue(result, "The is_subset function is incorrect for the case [1, 2, 3] and [1, 2, 3, 4, 5]")

    def test_example_case2(self):
        result = is_subset([1, 6], [1, 2, 3, 4, 5])
        self.assertFalse(result, "The is_subset function is incorrect for the case [1, 6] and [1, 2, 3, 4, 5]")

    def test_empty_list(self):
        result = is_subset([], [1, 2, 3])
        self.assertTrue(result, "The is_subset function is incorrect for the case of empty list")

if __name__ == '__main__':
    unittest.main()