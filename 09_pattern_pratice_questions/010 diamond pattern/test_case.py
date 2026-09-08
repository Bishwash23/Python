import unittest
from main import generate_diamond

class TestDiamondPattern(unittest.TestCase):
    
    def test_diamond_size_3(self):
        expected_output = ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
        self.assertEqual(generate_diamond(3), expected_output)

    def test_diamond_size_5(self):
        expected_output = ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
        self.assertEqual(generate_diamond(5), expected_output)
    
    def test_diamond_size_1(self):
        expected_output = ['*']
        self.assertEqual(generate_diamond(1), expected_output)

if __name__ == '__main__':
    unittest.main()