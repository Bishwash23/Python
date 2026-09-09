import unittest
from main import celsius_to_fahrenheit

class TestCelsiusToFahrenheit(unittest.TestCase):
    
    def test_zero_degrees(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_freezing_point(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_positive_value(self):
        self.assertEqual(celsius_to_fahrenheit(25), 77.0)

    def test_boiling_point(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

if __name__ == '__main__':
    unittest.main()