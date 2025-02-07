# Define the Figure classes
from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

# Create figure objects
shapes = [
    Rectangle(4, 5),
    Triangle(3, 4, 5),
    Circle(6)
]

# Calculate and output the area and perimeter of each figure
for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Area: {shape.get_area()}")
    print(f"  Perimeter: {shape.get_perimeter()}\n")
