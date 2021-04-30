import unittest
import get_weather


class TestInt2Degrees(unittest.TestCase):
    """Test convert int to degrees"""
    def test_positive(self):
        self.assertEqual(get_weather.int_to_degrees(100), '+100°')

    def test_negative(self):
        self.assertEqual(get_weather.int_to_degrees(-100), '-100°')

    def test_zero(self):
        self.assertEqual(get_weather.int_to_degrees(0), '0°')
