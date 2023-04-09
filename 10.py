class Summator:

    def transform(self, n):
        return n

    def sum(self, n):
        ret = 0
        for i in range(n):
            ret += self.transform(i + 1)
        return ret


class SquareSummator(Summator):

    def transform(self, n):
        return n**2


class CubeSummator(Summator):

    def transform(self, n):
        return n**3


print(Summator().sum(3))
print(SquareSummator().sum(3))
print(CubeSummator().sum(3))
