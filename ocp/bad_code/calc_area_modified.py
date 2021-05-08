from rectangle import Rectangle
from circle import Circle
class AreaCalculatorModified:
    """
     The original area calculator class modified to accomodate different shapes other than
     rectanngle.

     Now instead of just rectangle object, the area calculator method takes shape object
     and it checks for possible match with the help of if else condition
    """
    AREA = 0
    
    def area_calculator(self, shape):
        if(isinstance(shape,Rectangle)):
            self.AREA = shape.WIDTH * shape.HEIGHT
        elif(isinstance(shape,Circle)):
            self.AREA = 3.14 * shape.RADIUS * shape.RADIUS
        return self.AREA

circle = Circle(8)
area_calc_modified = AreaCalculatorModified()
print(area_calc_modified.area_calculator(circle))



