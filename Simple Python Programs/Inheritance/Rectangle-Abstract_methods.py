# Abstract Methods
from abc import ABC, abstractmethod
# Define Class Shape
class Shape(ABC):
    # define class printarea as an abstract class
    @abstractmethod
    def printarea(self):
        return 0
    
# Define Rectangle class as a subclass of Shape 
class Rectangle(Shape):
    # initialize Rectangle class
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    # define mandatory printarea function
    def printarea(self):
        return self.length*self.breadth

# initialize Rectangle class with required variables.       
rect = Rectangle(5,8)
print(f'Area of Rectangle is: {rect.printarea()}')