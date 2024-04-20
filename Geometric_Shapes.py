#This was made in April 2024 by Leo Platti
from math import pi
from math import sqrt

class GeometricShape():
    def __init__(self, name):
        self.__name = name
    def get_name(self):   
        return self.__name
    def set_name(self, name):
        self.__name = name
class Rectangle(GeometricShape):
    def __init__(self, length, width, name='Rectangle'):
        super().__init__("Rectangle")
        self.__length = length
        self.__width = width
    def get_length(self):
        return self.__length
    def set_length(self, length):
        self.__length = length
    def get_width(self):
        return self.__width
    def set_width(self, width):
        self.__width = width
    def get_perimeter(self):
        return 2 * self.__length + self.__width
    def get_area(self): 
        return self.__length * self.__width
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side, name='Square')
    def get_side(self):
        return self.get_length()
    def set_side(self, side):
        self.set_length(side)
        self.set_length(side)   

class Ellipse(GeometricShape):
    def __init__(self, semi_major_axis, semi_minor_axis, name='Ellipse'):
        super().__init__(name)
        self.__semi_major_axis = semi_major_axis
        self.__semi_minor_axis = semi_minor_axis
    def get_semi_major_axis(self):
        return self.__semi_major_axis
    def set_semi_major_axis(self, semi_major_axis):
        self.__semi_major_axis = semi_major_axis
    def get_semi_minor_axis(self):
        return self.__semi_minor_axis
    def set_semi_minor_axis(self, semi_minor_axis):
        self.__semi_minor_axis = semi_minor_axis
    def get_perimeter(self):
        return pi * (3 * (self.semi_major_axis + self.semi_minor_axis))
    def get_area(self):
        return self.semi_major_axis * self.semi_minor_axis * pi
class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius, name='Circle')
    def get_radius(self):
        return self.get_semi_major_axis()
    def set_radius(self, radius):
        self.set_semi_major_axis(radius)
        self.set_semi_minor_axis(radius)
