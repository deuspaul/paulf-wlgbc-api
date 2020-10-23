import unittest
from main import get_cityweather

class TestCity(unittest.TestCase):
    def test_types(self):
        #Make sure type errors are raised if anything but a string is entered
        self.assertRaises(TypeError, get_cityweather, True)
        self.assertRaises(TypeError, get_cityweather, 1)
