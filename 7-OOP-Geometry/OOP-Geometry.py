import math


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length + self.width) * 2


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
            (half_perimeter-self.b) * (half_perimeter-self.c)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return round(math.pi, 2) * self.radius * self.radius

    def get_perimeter(self):
        return self.radius * 2 * round(math.pi, 2)


class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return self.side * 4


circle = Circle(12)
square = Square(12)
triangle = Triangle(2, 3, 4)
rectangle = Rectangle(2, 5)
print("Rectangle area - " + str(rectangle.get_area()))
print("Rectangle perimeter - " + str(rectangle.get_perimeter()))
print("Triangle area - " + str(round(triangle.get_area(), 2)))
print("Triange perimeter - " + str(triangle.get_perimeter()))
print("Circle area - " + str(round(circle.get_area())))
print("Circle perimeter - " + str(circle.get_perimeter()))
print("Square area - " + str(square.get_area()))
print("Square perimeter - " + str(square.get_perimeter()))
