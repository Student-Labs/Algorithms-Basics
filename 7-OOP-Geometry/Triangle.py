import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        half_perimeter = self.get_perimeter() * 0.5
        return half_perimeter * \
            (half_perimeter - self.a) * \
            (half_perimeter - self.b) * (half_perimeter - self.c)
