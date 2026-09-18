import unittest
from main import count_even_odd

class TestCountEvenOdd(unittest.TestCase):

    def test_example_case1(self):
        result = count_even_odd([1, 2, 3, 4, 5])
        self.assertEqual(result, (2, 3), "The count_even_odd function is incorrect for the case [1, 2, 3, 4, 5]")

    def test_all_even(self):
        result = count_even_odd([2, 4, 6, 8, 10])
        self.assertEqual(result, (5, 0), "The count_even_odd function is incorrect for the case [2, 4, 6, 8, 10]")

    def test_all_odd(self):
        result = count_even_odd([1, 3, 5, 7, 9])
        self.assertEqual(result, (0, 5), "The count_even_odd function is incorrect for the case [1, 3, 5, 7, 9]")

if __name__ == '__main__':
    unittest.main()
