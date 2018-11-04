# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


def _get_range(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


class Triangle:
    def __init__(self, *args):
        self._A = args[0]
        self._B = args[1]
        self._C = args[2]

        self._set_props()

    def _set_props(self):
        self.AB = _get_range(self._A, self._B)
        self.BC = _get_range(self._B, self._C)
        self.AC = _get_range(self._A, self._C)
        self._p = self.AB + self.BC + self.AC
        self._h_ab = self._get_height(self.AB)
        self._h_bc = self._get_height(self.BC)
        self._h_ac = self._get_height(self.AC)
        self._area = self.AB * self._h_ab / 2

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        self._A = value
        self._set_props()

    @property
    def B(self):
        return self._B

    @B.setter
    def B(self, value):
        self._B = value
        self._set_props()

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, value):
        self._C = value
        self._set_props()

    @property
    def perimeter(self):
        return self._p

    @property
    def area(self):
        return self._area

    @property
    def heights(self):
        return {
            'AB': self._h_ab,
            'BC': self._h_bc,
            'AC': self._h_ac,
        }

    def _get_height(self, side):
        hp = self._p / 2
        return round(2 * math.sqrt(hp * (hp - self.AB) * (hp - self.BC) * (hp - self.AC)) / side, 9)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezium:
    def __init__(self, *args):
        self._points = {k: v for (k, v) in enumerate(args)}

        self._set_props()

    def _set_props(self):
        pts = self.points
        pts_cnt = len(pts)
        self._sides = [_get_range(pts.get(i), pts.get(i + 1) if i < pts_cnt - 1 else pts.get(0)) for i in range(pts_cnt)]
        self._p = sum(self.sides)
        self._h = self.points.get(1)[1] - self.points.get(0)[1]
        self._area = (self.sides[1] + self.sides[3]) * self.height / 2

    @property
    def points(self):
        return self._points

    @property
    def sides(self):
        return self._sides

    @property
    def perimeter(self):
        return self._p

    @property
    def area(self):
        return self._area

    @property
    def height(self):
        return self._h

    @property
    def is_isosceles(self):
        return self.points[1][0] - self.points[0][0] == self.points[3][0] - self.points[2][0]