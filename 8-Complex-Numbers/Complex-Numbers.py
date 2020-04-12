class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y,
                       self.x * other.y + self.y * other.x)

    def __truediv__(self, other):
        if self.x and self.y != 0 and other.x and other.y != 0:
            x1 = self.x * other.x + self.y * other.y
            x2 = other.x ** 2 + other.y ** 2
            y1 = other.x * self.y - self.x * other.y
            y2 = other.x ** 2 + other.y ** 2
            return Complex(x1 / x2, y1 / y2)

    def __str__(self):
        return '{} + {}i'.format(self.x, self.y)


x1 = Complex(13, -1)
x2 = Complex(7, -6)
print(str(x1 + x2))
print(str(x1 - x2))
print(str(x1 / x2))
print(str(x1 * x2))
