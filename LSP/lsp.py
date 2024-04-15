# LSP -> Liskov Substitution Principle
# Child class can take care of all the responsibilities -> that parent class can do
# In that case -> Child class Instance -> Can be substituted in place of parent class instance -> In real world program

# Why its Important ?
# Let us understand that -> Breaking down to 1st Principle -> Why do we need LSP
# Break it down to the most fundamental truth and then build from ground up there on

# classes as reusable building blocks for your code. A parent class defines a general blueprint,
# and subclasses inherit this blueprint with potentially added functionalities or specializations

# Subclasses are inherited from parent class -> so it has all the property of parent classes
# it should be able to execute all the functionalities of the parent and some added functionalities

# ex -> Parent class: Shape
# Subclass: Square

# Parent class Shape has calc_area() functionality to calculate the area of a shape
# when extended the cacl_area() function should calculate area in square class also

# If child class is not able to execute all the functionalities of the parent class -> means inheritance is not proper
