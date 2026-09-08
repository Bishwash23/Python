import unittest
from main import generate_hollow_square

class TestHollowSquarePattern(unittest.TestCase):
    
    def test_square_size_3(self):
        expected_output = ['***', '* *', '***']
        self.assertEqual(generate_hollow_square(3), expected_output)

    def test_square_size_5(self):
        expected_output = ['*****', '*   *', '*   *', '*   *', '*****']
        self.assertEqual(generate_hollow_square(5), expected_output)
    
    def test_square_size_2(self):
        expected_output = ['**', '**']
        self.assertEqual(generate_hollow_square(2), expected_output)
    
    def test_square_size_1(self):
        expected_output = ['*']
        self.assertEqual(generate_hollow_square(1), expected_output)

if __name__ == '__main__':
    unittest.main()