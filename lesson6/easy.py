# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, *args):
        self._A = args[0]
        self._B = args[1]
        self._C = args[2]

        self.set_props()

    def set_props(self):
        self.AB = Triangle._get_range(self._A, self._B)
        self.BC = Triangle._get_range(self._B, self._C)
        self.AC = Triangle._get_range(self._A, self._C)
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
        self.set_props()

    @property
    def B(self):
        return self._B

    @B.setter
    def B(self, value):
        self._B = value
        self.set_props()

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, value):
        self._C = value
        self.set_props()

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

    @staticmethod
    def _get_range(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def _get_height(self, side):
        hp = self._p / 2
        return round(2 * math.sqrt(hp * (hp - self.AB) * (hp - self.BC) * (hp - self.AC)) / side, 9)
