import unittest
from main import generate_right_angled_triangle

class TestRightAngledTrianglePattern(unittest.TestCase):
    
    def test_triangle_size_4(self):
        expected_output = ['   *', '  **', ' ***', '****']
        self.assertEqual(generate_right_angled_triangle(4), expected_output)

    def test_triangle_size_3(self):
        expected_output = ['  *', ' **', '***']
        self.assertEqual(generate_right_angled_triangle(3), expected_output)
    
    def test_triangle_size_1(self):
        expected_output = ['*']
        self.assertEqual(generate_right_angled_triangle(1), expected_output)

if __name__ == '__main__':
    unittest.main()