class Selector:

    def __init__(self, num_list):
        self.numbers = num_list

    def get_odds(self):
        return [i for i in self.numbers if i % 2 == 1]

    def get_evens(self):
        return [i for i in self.numbers if i % 2 == 0]


selector = Selector([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Get evens: ", *selector.get_evens())
print("Get odds: ", *selector.get_odds())
