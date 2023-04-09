class Queue:

    def __init__(self, *args):
        self.lst = []
        for i in args:
            self.lst.append(i)

    def append(self, *values):
        for i in values:
            self.lst.append(i)

    def copy(self):
        return Queue(*self.lst)

    def pop(self):
        if len(self.lst) > 0:
            return self.lst.pop(0)
        else:
            return None

    def extend(self, queue):
        self.lst.extend(queue.lst)

    def next(self):
        return Queue(*self.lst[1:])

    def __add__(self, other):
        return Queue(*self.lst, *other.lst)

#    def __iadd__(self, other):
#        self.extend(other)

    def __eq__(self, other):
        if len(self.lst) != len(other.lst):
            return False
        for i in range(len(self.lst)):
            if self.lst[i] != other.lst[i]:
                return False
        return True

    def __rshift__(self, other):
        if other > len(self.lst):
            return Queue()
        return Queue(*self.lst[other:])

    def __str__(self):
        return '[' + ''.join(["{} -> ".format(i) for i in self.lst]).rstrip(" -> ") + ']'

    def __next__(self):
        return self.next()


q1 = Queue(1, 2, 3)
print("q1: ", q1)
q1.append(4, 5)
print("q1 append: ", q1)
qx = q1.copy()
print("qx pop: ", qx.pop())
print("qx: ", qx)
q2 = q1.copy()
print("q2: ", q2)
print("q1 == q2 id\n{}    {}".format(q1 == q2, id(q1) == id(q2)))
q3 = q2.next()
print(q1, q2, q3, sep='\n----------\n')
print("q1 + q3: ", q1 + q3)
q3.extend(Queue(1, 2))
print("q3 extend: ", q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print("q4: ", q4)
q5 = next(q4)
print("q4: ", q4)
print("q5: ", q5)
