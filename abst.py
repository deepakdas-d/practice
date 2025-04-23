#Abstraction

from abc import ABC,abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass

class Circle():  # Concrete class
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):  # Concrete class
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2



# But you can instantiate the concrete classes:
circle = Circle(5)
print(circle.area())  # Output: 78.5

square = Square(4)
print(square.area())  # Output: 16
