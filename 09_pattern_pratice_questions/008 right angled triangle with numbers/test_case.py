import unittest
from main import generate_number_triangle

class TestNumberTrianglePattern(unittest.TestCase):
    
    def test_triangle_size_5(self):
        expected_output = ['1', '22', '333', '4444', '55555']
        self.assertEqual(generate_number_triangle(5), expected_output)

    def test_triangle_size_3(self):
        expected_output = ['1', '22', '333']
        self.assertEqual(generate_number_triangle(3), expected_output)
    
    def test_triangle_size_1(self):
        expected_output = ['1']
        self.assertEqual(generate_number_triangle(1), expected_output)

if __name__ == '__main__':
    unittest.main()