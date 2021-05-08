from shape import Shape
from rectangle import Rectangle
from circle import Circle

class AreaCalculator:
    """
      In this class just pass the shape, and for any shape passed 
      Call the area method of that shape.
    """

    def area(self, shape):
        return shape.area()


rectangle = Rectangle(8,10)
circle = Circle(6)
calc_area = AreaCalculator()
print(calc_area.area(rectangle))
print(calc_area.area(circle))
