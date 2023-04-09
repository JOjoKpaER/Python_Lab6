class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        Triangle.__init__(self, a, a, a)


et = EquilateralTriangle(2)
print(et.perimeter())
