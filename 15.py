from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Vector(Shape):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return abs(self.x * self.y)

    # Operator +
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Operator ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Operator <
    def __lt__(self, other):
        return self.area() < other.area()

    # Operator string representation
    def __str__(self):
        return f"({self.x}, {self.y})"


# Create objects
v1 = Vector(3, 4)
v2 = Vector(2, 5)

# Addition
v3 = v1 + v2

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Addition:", v3)

# Area
print("Area of Vector 1:", v1.area())
print("Area of Vector 2:", v2.area())

# Comparison
print("Are vectors equal?", v1 == v2)
print("Is Vector 1 smaller?", v1 < v2)