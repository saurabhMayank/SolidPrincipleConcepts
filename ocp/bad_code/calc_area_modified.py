from rectangle import Rectangle
from circle import Circle
import math
class AreaCalculatorModified:
    """
     The original area calculator class modified to accomodate different shapes other than
     rectanngle.

     Now instead of just rectangle object, the area calculator method takes shape object
     and it checks for possible match with the help of if else condition


     The more the shapes increases, the if else cases will be added to this particular function
     Problems in that
     -> Same function modified everytime, everytime a new responsibility added
     -> As different responsibilties added, no seperation of concerns, function can be modified for multiple reasons
     -> Leading to increases chances of bug, too much logic crammed in one function, leading to poor devX
    """
    AREA = 0
    
    def area_calculator(self, shape):
        if(isinstance(shape,Rectangle)):
            self.AREA = shape.WIDTH * shape.HEIGHT
        elif(isinstance(shape,Circle)):
            self.AREA = math.pi * shape.RADIUS * shape.RADIUS
        return self.AREA

circle = Circle(8)
area_calc_modified = AreaCalculatorModified()
print(area_calc_modified.area_calculator(circle))



