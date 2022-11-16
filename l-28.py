

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Мagic method
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


    def draw(self):
        print(f"Point ({self.x}, {self.y})")


print()

point = Point(1, 2)

point.draw()

print(point)


point2 = Point(1, 2)


print(point == point2) # --> False