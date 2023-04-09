class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y


p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(1, 1)

print("p1 Equal p2: ", p1 == p2)
print("p1 Equal p3: ", p1 == p3)
print("p1 Not Equal p2: ", p1 != p2)
print("p1 Not Equal p3: ", p1 != p3)

