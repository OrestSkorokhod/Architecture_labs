import unittest

from  lab1_reflection import Triangle, Quadrilateral


class TestHomework(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(Triangle(a=3, b=4, c=5).get_area(), 6)

    def test_area_2(self):
        self.assertEqual(Triangle(a=6, b=8, c=10).get_area(), 24)

    def test_area_3(self):
        self.assertEqual(Triangle(a=5, b=9, c=1).get_area(), 6)

    def test_area_4(self):
        self.assertEqual(Quadrilateral(a=3, b=4, c=3, d=4, diagonal=5).get_area(), 12)

    def test_area_5(self):
            self.assertEqual(Quadrilateral(a=3, b=4, c=3, d=4, diagonal=5).get_area(), 24)

    def test_area_empty_1(self):
        self.assertEqual(Triangle(a=0, b=0, c=0).get_area(), 0)

    def test_area_empty_2(self):
        self.assertEqual(Triangle(a=0, b=0, c=0).get_area(), 5)

    def test_area_empty_3(self):
        self.assertEqual(Quadrilateral(a=0, b=0, c=0, d=0, diagonal=0).get_area(), 0)


if __name__ == '__main__':
    unittest.main()
