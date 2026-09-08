import unittest
from main import generate_pyramid

class TestPyramidPattern(unittest.TestCase):
    
    def test_pyramid_size_3(self):
        expected_output = ['  *  ', ' *** ', '*****']
        self.assertEqual(generate_pyramid(3), expected_output)

    def test_pyramid_size_5(self):
        expected_output = ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
        self.assertEqual(generate_pyramid(5), expected_output)
    
    def test_pyramid_size_1(self):
        expected_output = ['*']
        self.assertEqual(generate_pyramid(1), expected_output)

if __name__ == '__main__':
    unittest.main()