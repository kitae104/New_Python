from Basic_WS.inheritance.GeometricObject import GeometricObject
import math

class Circle(GeometricObject):

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def getDiameter(self):
        return 2 * self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def printCircle(self):
        print(self.__str__() + " 반지름 : " + str(self.__radius))

    def __str__(self):
        return super().__str__() + ", 반지름 : " + str(self.__radius)