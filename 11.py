class Summator:

    def transform(self, n):
        return n

    def sum(self, n):
        ret = 0
        for i in range(n):
            ret += self.transform(i + 1)
        return ret


class PowerSummator(Summator):

    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n**self.b


class SquareSummator(PowerSummator):

    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):

    def __init__(self):
        super().__init__(3)


print(PowerSummator(0.5).sum(3))
print(SquareSummator().sum(3))
print(CubeSummator().sum(3))
