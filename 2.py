class Balance:

    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def result(self):
        if self.right == self.left:
            return "="
        if self.right > self.left:
            return "R"
        else:
            return "L"


balance0 = Balance()
balance0.add_right(12)
balance0.add_left(9)
balance0.add_left(2)
print("Balance0: " + balance0.result())

balance1 = Balance()
balance1.add_right(10)
balance1.add_left(5)
balance1.add_left(5)
print("Balance1: " + balance1.result())
balance1.add_left(1)
print("Balance1: " + balance1.result())
