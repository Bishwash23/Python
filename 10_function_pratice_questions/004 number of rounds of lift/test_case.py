import unittest
from main import calculate_lift_rounds

class TestLiftRounds(unittest.TestCase):
    
    def test_lift_rounds(self):
        self.assertEqual(calculate_lift_rounds(10, 3), 4)
        self.assertEqual(calculate_lift_rounds(7, 4), 2)
        self.assertEqual(calculate_lift_rounds(100, 10), 10)
        self.assertEqual(calculate_lift_rounds(5, 5), 1)

if __name__ == '__main__':
    unittest.main()