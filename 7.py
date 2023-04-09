class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        if len(self.coefficients) > len(other.coefficients):
            for i in range(len(other.coefficients)):
                self.coefficients += other.coefficients
                return self
        else:
            sum_coef = other.coefficients
            for i in range(len(self.coefficients)):
                sum_coef[i] += self.coefficients[i]
            self.coefficients = sum_coef
            return self

    def poly(self, x):
        res = 0
        for i in range(len(self.coefficients)):
            res += x**i * self.coefficients[i]
        return res


poly1 = Polynomial([1, 1])
poly2 = Polynomial([0, 1, 2])
print(poly1.poly(2))
print(poly2.poly(1))
poly3 = poly1 + poly2
print(poly3.poly(3))
