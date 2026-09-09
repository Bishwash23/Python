import unittest
from main import area_of_rectangle

class TestAreaOfRectangle(unittest.TestCase):
    
    def test_area_of_rectangle(self):
        self.assertEqual(area_of_rectangle(5, 3), 15.0)
        self.assertEqual(area_of_rectangle(7.5, 2.4), 18.0)
        self.assertEqual(area_of_rectangle(10, 10), 100.0)

if __name__ == '__main__':
    unittest.main()