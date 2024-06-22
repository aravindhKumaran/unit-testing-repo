import math 
from typing import *


class Shape:

    def area(self):
        pass 

    def perimeter(self):
        pass 


class Circle(Shape):

    def __init__(self, radius: Union[int, float]):
        self.radius = radius 

    def area(self) -> Union[int, float]:
        return math.pi * self.radius ** 2
    

    def perimeter(self) -> Union[int, float]:
        return 2 * math.pi * self.radius 


class Rectangle:

    def __init__(self, length: Union[int, float], width: Union[int, float]):
        self.length = length 
        self.width = width 


    def area(self) -> Union[int, float]:
        return self.length * self.width

    def perimeter(self) -> Union[int, float]:
        return (self.length * 2) + (self.width * 2)

class Square(Rectangle):
    # Inherits Rectangle Class

    def __init__(self, side_length):
        # Initialize Rectangle constructor
        super().__init__(side_length, side_length)
