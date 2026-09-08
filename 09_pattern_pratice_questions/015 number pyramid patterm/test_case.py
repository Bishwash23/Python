import unittest
from main import generate_number_pyramid

class TestNumberPyramidPattern(unittest.TestCase):
    
    def test_pyramid_size_4(self):
        expected_output = ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
        self.assertEqual(generate_number_pyramid(4), expected_output)

    def test_pyramid_size_3(self):
        expected_output = ['  1  ', ' 1 2 ', '1 2 3']
        self.assertEqual(generate_number_pyramid(3), expected_output)
    
    def test_pyramid_size_1(self):
        expected_output = ['1']
        self.assertEqual(generate_number_pyramid(1), expected_output)

if __name__ == '__main__':
    unittest.main()