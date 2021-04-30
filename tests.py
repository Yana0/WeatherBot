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


class TestInt2Degrees(unittest.TestCase):
    """Test convert int to degrees"""
    def test_positive(self):
        self.assertEqual(get_weather.int_to_degrees(100), '+100°')

    def test_negative(self):
        self.assertEqual(get_weather.int_to_degrees(-100), '-100°')

    def test_zero(self):
        self.assertEqual(get_weather.int_to_degrees(0), '0°')


def test_all():
    suite = unittest.TestSuite()
    suite.addTest(TestDegrees2Int('test_positive'))
    suite.addTest(TestDegrees2Int('test_negative'))
    suite.addTest(TestDegrees2Int('test_zero'))
    suite.addTest(TestInt2Degrees('test_positive'))
    suite.addTest(TestInt2Degrees('test_negative'))
    suite.addTest(TestInt2Degrees('test_zero'))
