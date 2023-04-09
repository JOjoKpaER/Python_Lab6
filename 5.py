class ReversedList:

    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, item):
        return self.lst[-item-1]

    def __len__(self):
        return len(self.lst)


rl = ReversedList([10, 20, 30])
print(*[rl[i] for i in range(len(rl))])
print(rl[0])
