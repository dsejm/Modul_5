class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        print((self.x ** 2 + self.y ** 2) ** (1 / 2))

    def __add__(self, other):
        print(self.x + other.x, self.y + other.y)

p1 = Point(1, 1)
p2 = Point(7, 8)
p1.distance()
p2.distance()
p3 = p1 + p2
