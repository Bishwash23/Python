import unittest
from main import check_unique

class TestCheckUnique(unittest.TestCase):

    def test_example_case1(self):
        result = check_unique([1, 2, 3, 4, 5])
        self.assertTrue(result, "The check_unique function is incorrect for the case [1, 2, 3, 4, 5]")

    def test_example_case2(self):
        result = check_unique([1, 2, 3, 3, 4, 5])
        self.assertFalse(result, "The check_unique function is incorrect for the case [1, 2, 3, 3, 4, 5]")

    def test_example_case3(self):
        result = check_unique([1, 1, 1, 1])
        self.assertFalse(result, "The check_unique function is incorrect for the case [1, 1, 1, 1]")

if __name__ == '__main__':
    unittest.main()