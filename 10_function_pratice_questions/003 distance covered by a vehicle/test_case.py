import unittest
from main import calculate_distance

class TestCalculateDistance(unittest.TestCase):
    
    def test_distance_traveled(self):
        self.assertEqual(calculate_distance(60, 2), 120.0)
        self.assertEqual(calculate_distance(50.5, 1.5), 75.75)
        self.assertEqual(calculate_distance(80, 1.25), 100.0)
        self.assertEqual(calculate_distance(30, 0.5), 15.0)

if __name__ == '__main__':
    unittest.main()