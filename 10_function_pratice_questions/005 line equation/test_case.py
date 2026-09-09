import unittest
from main import calculate_y

class TestCalculateY(unittest.TestCase):
    
    def test_y_value(self):
        self.assertEqual(calculate_y(2, 3, 4), 11.0)
        self.assertEqual(calculate_y(1.5, -2, 2), 1.0)
        self.assertEqual(calculate_y(0, 5, 10), 5.0)
        self.assertEqual(calculate_y(-1, 3, 6), -3.0)

if __name__ == '__main__':
    unittest.main()