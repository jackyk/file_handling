from abc import ABCMeta, abstractmethod

class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def area():pass

    @abstractmethod
    def perimeter():pass
'''
The abstractmethods help the class Rectangle to have all the recquierements that the super class contains
'''
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super(Rectangle, self).__init__
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width*2 + self.height*2

class Square(Rectangle):
    def __init__(self, sidelength):
        self.sidelength = sidelength
        super(Square, self).__init__(sidelength, sidelength)

# rect = Rectangle(5, 10)
# print rect.area()
# print rect.perimeter()

s = Square(5)
print s.area()
print s.perimeter()


# How to use abstraction and interfaces and also how to to overide

# rect = Rectangle(6,10)
# print rect.area()
# print rect.perimeter()
# test_1 = Shape()
# test_1.area()
