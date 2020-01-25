import math


class Circle:
    def __init__(self, radius, result=0):
        self.radius = radius

    def get_area(self):
        self.result = round(math.pi, 2) * self.radius * self.radius
        return self.result

    def get_perimeter(self):
        self.result = self.radius * 2*round(math.pi, 2)
        return self.result


class Square:
    def __init__(self, side, result=0):
        self.side = side

    def get_area(self):
        self.result = self.side * self.side
        return self.result

    def get_perimeter(self):
        self.result = self.side *4
        return self.result


circle = Circle(12)
square = Square(12)
print("Circle area - " + str(round(circle.get_area())))
print("Square area - " + str(square.get_area()))
print("Square perimeter - " + str(square.get_perimeter()))
print("Corcle perimeter - " + str(circle.get_perimeter()))
