from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def calculate_area(self):
        area=self.side*self.side
        return area

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        area=self.length*self.width
        return area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        area=math.pi*self.radius*self.radius
        return area

s = Square(4)
r = Rectangle(3, 5)
c = Circle(7)
print(s.calculate_area())
print(r.calculate_area())
print(c.calculate_area())