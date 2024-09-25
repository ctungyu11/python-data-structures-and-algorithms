"""_summary_:
This module contains classes that represent geometric shapes.

_classes_:
- Shape: The base class for all shapes.
- Circle: A class representing a circle.
- Rectangle: A class representing a rectangle.
- Square: A class representing a square.
- Triangle: A class representing a triangle.

_functions_:
- shape_factory: A factory function that creates a shape based on the given parameters.
"""

from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):
    """A base class for all shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """A class representing a circle."""

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * pi * self.radius


class Rectangle(Shape):
    """A class representing a rectangle."""
    
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Square(Rectangle):
    """A class representing a square."""
    
    def __init__(self, side: float):
        super().__init__(side, side)
    

class Triangle(Shape):
    """A class representing a triangle."""
    
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        
        self.a = a
        self.b = b
        self.c = c
    
    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c
    

def shape_factory(shape_type: str, *args) -> Shape:
    """Create a shape based on the given parameters."""
    
    if shape_type == "circle":
        return Circle(*args)
    elif shape_type == "rectangle":
        return Rectangle(*args)
    elif shape_type == "square":
        return Square(*args)
    elif shape_type == "triangle":
        return Triangle(*args)
    
    raise ValueError("Invalid shape type")


if __name__ == "__main__":
    shapes : list[Shape] = [
        shape_factory("circle", 3.0),
        shape_factory("rectangle", 2.0, 4.0),
        shape_factory("square", 2.0),
        shape_factory("triangle", 3.0, 4.0, 5.0)
    ]
    
    for shape in shapes:
        shape_name = shape.__class__.__name__
        print(f"{shape_name}:")
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
        print()
