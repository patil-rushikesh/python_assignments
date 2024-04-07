class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        return Complex((self.real * other.real + self.imag * other.imag) / denominator,
                       (self.imag * other.real - self.real * other.imag) / denominator)

    def print(self):
        print(f'{self.real} + {self.imag}i')

if __name__ == "__main__":
    a = Complex(10, 12)
    b = Complex(4, 5)
    c = a + b
    c.print()
    c = a - b
    c.print()
    c = a * b
    c.print()
    c = a / b
    c.print()
