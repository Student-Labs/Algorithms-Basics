import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return round(math.pi, 2) * self.radius * self.radius

    def get_perimeter(self):
        return self.radius * 2 * round(math.pi, 2)
