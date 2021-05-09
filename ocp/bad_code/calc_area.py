from rectangle import Rectangle

class AreaCalculator:
    """
      Area calculator class.
      A particular shape is passed as an argument..
      Calculates the area given the shape.. Calculates the area based on the shape..

      So the problem with this class is
      i) There is no uniformity in the area of different shapes...
      ii) So based on a particular shape it has to make if else cases to define the logic
        for area calculation.
      iii) When a lot of shapes increase then if else cases also increase a lot.
      iv) This makes the code a lot rigid because everytime a shape is passed,
          it has to be checked at every if else case for possible match.
      v) This checking leads to the recompilation of all the shape classes, which signifies
         rigidity.
      vi) Let's say tomorrow I add another class circle and I start calculating its shape.
      vii) And then oval.
      ix) After sometime I add another class rotateShapes which rotates the shapes. Let's say I can rotate all the shapes but not circle and some programmer failed to add the case for circle, So in rotate all shape if circle will come it will break.
      That is fragile code.

      More from this lecture of DR BOB
      https://www.youtube.com/watch?v=zHiWqnTWsn4&t=3204s&ab_channel=FucktheCommunism
      at time 1:06:48
    """

    def area_calculator(self, rectangle):
        """
         calculates area based on given shape
        """
        return rectangle.WIDTH*rectangle.HEIGHT

rectangle = Rectangle(9,10)
areaCalc = AreaCalculator()
print(areaCalc.area_calculator(rectangle))