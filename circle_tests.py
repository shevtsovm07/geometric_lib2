import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive_radius(self):
        res = area(5)
        self.assertEqual(res, math.pi * 25)

    def test_area_large_radius(self):
        res = area(10)
        self.assertEqual(res, math.pi * 100)

    def test_area_float_radius(self):
        res = area(2.5)
        self.assertEqual(res, math.pi * 6.25)

    def test_perimeter_zero_radius(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_radius(self):
        res = perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)

    def test_perimeter_large_radius(self):
        res = perimeter(10)
        self.assertEqual(res, 2 * math.pi * 10)

    def test_perimeter_float_radius(self):
        res = perimeter(3.5)
        self.assertEqual(res, 2 * math.pi * 3.5)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

if __name__ == '__main__':
    unittest.main()