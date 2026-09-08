import unittest
from main import generate_inverted_triangle

class TestInvertedTrianglePattern(unittest.TestCase):
    
    def test_triangle_size_3(self):
        expected_output = ['***', '**', '*']
        self.assertEqual(generate_inverted_triangle(3), expected_output)

    def test_triangle_size_5(self):
        expected_output = ['*****', '****', '***', '**', '*']
        self.assertEqual(generate_inverted_triangle(5), expected_output)
    
    def test_triangle_size_1(self):
        expected_output = ['*']
        self.assertEqual(generate_inverted_triangle(1), expected_output)

if __name__ == '__main__':
    unittest.main()