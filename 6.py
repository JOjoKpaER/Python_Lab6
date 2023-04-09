class SparseArray:

    def __init__(self):
        self.array = {}
        self.length = 0

    def __setitem__(self, key, value):
        if key > self.length:
            self.length = key + 1
        self.array.update({key: value})

    def __getitem__(self, item):
        if item not in self.array.keys():
            return 0
        else:
            return self.array[item]

    def __len__(self):
        return self.length

    def print_keys(self):
        print(self.array.keys())


arr = SparseArray()
arr[3] = 5
arr[20] = 10
arr[8] = 15
print(*[arr[i] for i in range(len(arr))])
arr[88005553535] = 99
print(arr[88005553535])
print(arr[88005553535+1])
