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
            return Complex((self.x * other.x + self.y * other.y)
                           / (other.x ** 2 + other.y ** 2),
                           ((other.x * self.y - self.x * other.y) / (other.x ** 2 + other.y ** 2)))

    def __str__(self):
        return '{} + {}i'.format(self.x, self.y)


x1 = Complex(1, 1)
x2 = Complex(1, 1)
print(str(x1 + x2))
print(str(x1 - x2))
print(str(x1 / x2))
print(str(x1 * x2))
