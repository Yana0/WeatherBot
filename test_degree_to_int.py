import unittest
import get_weather


class TestDegrees2Int(unittest.TestCase):
    """Test convert degrees to int"""
    def test_positive(self):
        self.assertEqual(get_weather.degrees_to_int(' +10° '), [10])

    def test_negative(self):
        self.assertEqual(get_weather.degrees_to_int(' -10° '), [-10])

    def test_zero(self):
        self.assertEqual(get_weather.degrees_to_int(' 0° '), [0])
