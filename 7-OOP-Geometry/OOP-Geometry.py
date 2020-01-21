import math


class Circle:
    def __init__(self, radius, result=0):
        self.radius = radius

    def get_area(self):
        self.result = round(math.pi, 2) * self.radius * self.radius
        return self.result


class Square:
    def __init__(self, side, result=0):
        self.side = side

    def get_area(self):
        self.result = self.side * self.side
        return self.result


circle_area = Circle(12)
square_area = Square(12)
print(round(circle_area.get_area()))
print(square_area.get_area())
