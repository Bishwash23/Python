import unittest
from main import reverse_list

class TestReverseList(unittest.TestCase):

    def test_example_case1(self):
        result = reverse_list([1, 2, 3, 4, 5])
        self.assertEqual(result, [5, 4, 3, 2, 1], "The reverse_list function is incorrect for the case [1, 2, 3, 4, 5]")

    def test_single_element(self):
        result = reverse_list([10])
        self.assertEqual(result, [10], "The reverse_list function is incorrect for the case [10]")

    def test_empty_list(self):
        result = reverse_list([])
        self.assertEqual(result, [], "The reverse_list function is incorrect for the case []")

if __name__ == '__main__':
    unittest.main()