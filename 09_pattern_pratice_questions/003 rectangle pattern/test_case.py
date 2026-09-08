import unittest
from main import generate_rectangle

class TestRectanglePattern(unittest.TestCase):
    
    def test_rectangle_size_4x5(self):
        expected_output = ['*****', '*****', '*****', '*****']
        self.assertEqual(generate_rectangle(4, 5), expected_output)

    def test_rectangle_size_3x2(self):
        expected_output = ['**', '**', '**']
        self.assertEqual(generate_rectangle(3, 2), expected_output)

    def test_rectangle_size_1x1(self):
        expected_output = ['*']
        self.assertEqual(generate_rectangle(1, 1), expected_output)

if __name__ == '__main__':
    unittest.main()