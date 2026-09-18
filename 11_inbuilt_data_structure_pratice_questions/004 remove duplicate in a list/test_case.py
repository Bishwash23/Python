import unittest
from main import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_example_case1(self):
        result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5], "The remove_duplicates function is incorrect for the case [1, 2, 2, 3, 4, 4, 5]")

    def test_example_case2(self):
        result = remove_duplicates([4, 5, 5, 4, 6, 7])
        self.assertEqual(result, [4, 5, 6, 7], "The remove_duplicates function is incorrect for the case [4, 5, 5, 4, 6, 7]")

    def test_example_case3(self):
        result = remove_duplicates([1, 1, 1, 1, 1])
        self.assertEqual(result, [1], "The remove_duplicates function is incorrect for the case [1, 1, 1, 1, 1]")

if __name__ == '__main__':
    unittest.main()