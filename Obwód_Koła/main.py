class Circle:
    def __init__(self, r):
        self.r = r
        self.pi = 3.14

    def area(self):
        return self.pi * self.r * self.r

    def perimeter(self):
        return 2 * self.pi * self.r


circle = Circle(6)
print(circle.area())
print(circle.perimeter())