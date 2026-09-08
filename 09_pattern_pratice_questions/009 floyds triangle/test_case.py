import unittest
from main import generate_floyds_triangle

class TestFloydsTriangle(unittest.TestCase):
    
    def test_triangle_size_5(self):
        expected_output = ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']
        self.assertEqual(generate_floyds_triangle(5), expected_output)

    def test_triangle_size_3(self):
        expected_output = ['1', '2 3', '4 5 6']
        self.assertEqual(generate_floyds_triangle(3), expected_output)
    
    def test_triangle_size_1(self):
        expected_output = ['1']
        self.assertEqual(generate_floyds_triangle(1), expected_output)

if __name__ == '__main__':
    unittest.main()