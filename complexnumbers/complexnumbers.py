class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # magic or dunder method overides the default method
    def __add__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __sub__(self, other):
        return Complex(self.left - other.left, self.right - other.right)

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __gt__(self, other):
        return self.left > other.left and self.right > other.right

    def __iadd__(self, other):
        self.left += other.left
        self.right += other.right
        return Complex(self.left, self.right)

    def __isub__(self, other):
        self.left -= other.left
        self.right += other.right
        return Complex(self.left, self.right)

    def __repr__(self):
        return f'{self.left}j {'+' if self.right > 0 else "-"} {abs(self.right)}i'


a = Complex(2, 3)
b = Complex(5, 5)
d = Complex(5, 5)
print(a)
print(b)
c = a + b

print(c)
print(a - b)
print(a == d)
print(a != d)
print(b > a)
print(b == d)
print(a)
print(b)
a += b
print(a)
a -= b
print(a)
