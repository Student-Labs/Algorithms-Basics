import math


class Rectangle:
    def __init__(self, width, length, result=0):
        self.width = width
        self.length = length

    def get_area(self):
        self.result = self.length * self.width
        return self.result

    def get_perimeter(self):
        self.result = (self.length + self.width) * 2
        return self.result


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        self.result = self.a + self.b + self.c
        return self.result

    def get_area(self):
        half_perimeter = Triangle.get_perimeter(self) * 0.5
        self.result = half_perimeter * \
            (half_perimeter - self.a) * \
            (half_perimeter-self.b) * (half_perimeter-self.c)
        return round(self.result, 2)


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
        self.result = self.side * 4
        return self.result


circle = Circle(12)
square = Square(12)
triangle = Triangle(2, 3, 4)
rectangle = Rectangle(2, 5)
print("Rectangle area - " + str(rectangle.get_area()))
print("Rectangle perimeter - " + str(rectangle.get_perimeter()))
print("Triangle area - " + str(triangle.get_area()))
print("Triange perimeter - " + str(triangle.get_perimeter()))
print("Circle area - " + str(round(circle.get_area())))
print("Circle perimeter - " + str(circle.get_perimeter()))
print("Square area - " + str(square.get_area()))
print("Square perimeter - " + str(square.get_perimeter()))
