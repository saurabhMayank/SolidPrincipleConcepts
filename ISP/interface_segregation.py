"""
What is interface segregation ?

Classes should not be depend on methods in the interface which they do not use. This principle is used to solve the fat interfaces problem

Why it is important ? Let's break it down to the first principle ?

Remember SRP -> Single Responsibility of Class and Function, Class and Function should have 1 reason to change. So that class and function are not fragile

ISP Agenda -> Interfaces should be small and should only have methods that the implementing classes needs, it should not have methods that classes implementing it have no use

It is important to maintain loose coupling

"""

"""
I have a mobile applications with different types of views
-> Profile View
-> User details View
etcetra

Different types of views will use different types of gestures on it
"""

"""
Lets say a developer is told to create a gesture interface
-> As requirement in User Profile View 
-> User can tap on user profile and see the `user profile view` and see details of the user
"""

# global base classes for abstract class
from ABC import abc

class Gesture(abc):
  pass
