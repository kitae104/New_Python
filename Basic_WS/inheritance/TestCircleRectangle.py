from Basic_WS.inheritance.CircleFromGeometricObject import Circle
from Basic_WS.inheritance.RectangleFromGeometricObject import Rectangle

def main():
    circle = Circle(1.5)
    circle.setColor("red")
    print("원", circle)
    print("반지름 : ", circle.getRadius())
    print("넓이 : ", circle.getArea())
    print("지름 : ", circle.getDiameter())

    rectangle = Rectangle(2, 4)
    print("\n사각형", rectangle)
    print("넓이 : ", rectangle.getArea())
    print("둘레 : ", rectangle.getPerimeter())

main()