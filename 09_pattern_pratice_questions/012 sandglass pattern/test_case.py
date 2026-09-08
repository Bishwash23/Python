import unittest
from main import generate_sandglass

class TestSandglassPattern(unittest.TestCase):
    
    def test_sandglass_size_3(self):
        expected_output = ['*****', ' *** ', '  *  ', ' *** ', '*****']
        self.assertEqual(generate_sandglass(3), expected_output)

    def test_sandglass_size_4(self):
        expected_output = ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
        self.assertEqual(generate_sandglass(4), expected_output)
    
    def test_sandglass_size_1(self):
        expected_output = ['*']
        self.assertEqual(generate_sandglass(1), expected_output)

if __name__ == '__main__':
    unittest.main()