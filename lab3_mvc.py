import unittest
from mockito import when, mock, unstub

from lab1_reflection import Triangle
from lab1_reflection import Quadrilateral

class Controller:
    model = None
    view = None
    def __init__(self, view):
        self.view = view
    def set_model(self, model):
        self.model = model
    def set_sides(self, a, b, c, d):
        triangle = Triangle(a, b, c)
        self.model = Quadrilateral(triangle, d)
        self.model = triangle
    def get_model(self):
        return self.model
    def show(self):
        return self.view.show(self.model)
    def get_sides(self):
        return self.model.get_sides()

class View:
    def show(self, model):
        print(model)


class ControllerTest(unittest.TestCase):
    def test_get_sides_with_mock(self):
        triangle = Triangle(3, 3, 3)
        kvadrat = Quadrilateral(triangle, 3)
        when(kvadrat).get_sides().thenReturn((5, 5, 5, 5))
        view = View()
        controller = Controller(view)
        controller.set_model(kvadrat)
        self.assertEqual(kvadrat.get_sides(), (5, 5, 5, 5))

    def test_get_perimetr_with_mock(self):
        triangle = Triangle(3, 3, 3)
        kvadrat = Quadrilateral(triangle, 3)
        when(kvadrat).get_perimetr().thenReturn(15)
        view = View()
        controller = Controller(view)
        controller.set_model(kvadrat)
        self.assertEqual(kvadrat.get_perimetr(), 12)

    def test1(self):
        self.assertEqual(15, 15)

if __name__ == '__main__':
    unittest.main()
