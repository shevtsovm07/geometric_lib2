import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive_side(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_large_side(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_float_side(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_perimeter_zero_side(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_side(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_large_side(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_float_side(self):
        res = perimeter(3.5)
        self.assertEqual(res, 14.0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == '__main__':
    unittest.main()