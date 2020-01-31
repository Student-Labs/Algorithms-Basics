class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Complex(self.x / other.x, self.y / other.y)

    def __str__(self):
        return '{} + {}i'.format(self.x, self.y)


x1 = Complex(1, 3)
x2 = Complex(2, 3)
print(str(x1 + x2))
print(str(x1 - x2))
print(str(x1 / x2))
print(str(x1 * x2))
