import unittest
from main import generate_hollow_inverted_right_angled_triangle

class TestHollowInvertedRightAngledTrianglePattern(unittest.TestCase):
    
    def test_triangle_size_4(self):
        expected_output = ['****', '* *', '**', '*']
        self.assertEqual(generate_hollow_inverted_right_angled_triangle(4), expected_output)

    def test_triangle_size_5(self):
        expected_output = ['*****', '*  *', '* *', '**', '*']
        self.assertEqual(generate_hollow_inverted_right_angled_triangle(5), expected_output)
    
    def test_triangle_size_1(self):
        expected_output = ['*']
        self.assertEqual(generate_hollow_inverted_right_angled_triangle(1), expected_output)

if __name__ == '__main__':
    unittest.main()