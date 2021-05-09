from shape import Shape
class Rectangle(Shape):
    """
     Class Rectangle representing the geometric shape rectangle
     Sets the width and height of the rectangle in the constructor.

     This geometric class will inherit the abstract class shape
    """
    WIDTH = 0
    HEIGHT = 0

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
    
    def area(self):
        return self.WIDTH * self.HEIGHT 