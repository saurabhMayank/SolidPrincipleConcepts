"""
What is interface segregation ?

Classes should not be depend on methods in the interface which they do not use. This principle is used to solve the fat interfaces problem

Why it is important ? Let's break it down to the first principle ?

Remember SRP -> Single Responsibility of Class and Function, Class and Function should have 1 reason to change. 
So that class and function are not fragile

ISP Agenda -> Interfaces should be small and should only have methods that the implementing classes needs, 
it should not have methods that classes implementing it have no use

It is important to maintain loose coupling

"""

"""
I have a mobile applications with different types of views
-> Profile Picture View
-> User details View
etcetra

Different types of views will use different types of gestures on it
"""

"""
Lets say a developer is told to create a gesture interface
-> As requirement in User Details View 
-> User can tap on user userdetail icon -> it will open `user details view` and see details of the user

-> Only one gesture required here i.e. Single Tap
"""

# global base classes for abstract class
# in python, interface is implemented using abstract classes
from ABC import abc

class Gesture(abc):

  def __init__(self):
    pass

  def one_tap(self):
    pass


class UserDetailsView(Gesture):

  def __init__(self):
    pass

  
  def one_tap(self):
    # open user details view of the user
    # see the name of the user



"""
Now the product manager comes and tells that listen -> we also need to implement a profilepicture view

A user can do a single tap -> On profile picture -> The profile picture will come in full screen
A user can do double tap -> On profile picture -> The profile picture will be zoomed in
A user can do long tap -> On profile picture -> The profile picture will be downloaded

Developer thinks that -> ok an interface Gesture is already, lets go and change the same interface
and implement it to -> ProfilePictureView class

"""

# modified Gesture interface

class Gesture(abc):

  def __init__(self):
    pass

  def one_tap(self):
    pass
  
  def double_tap(self):
    pass
  
  def long_press(self):
    pass


class ProfilePictureView(Gesture):

  def __init__(self):
    pass
  
  def one_tap(self):
    # open profile picture in full screen
  
  def double_tap(self):
    # zoom in profile picture
  
  def long_press(self):
    # download the profile picture


"""
But the developer made a mistake here 
-> The developer did not see that the Gesture interface is already implement on
UserDetailsView Class -> which requires only single tap gesture

-> So the code started breaking as UserDetailsView class did not implement other Gesture interface methods

-> So the developer went ahead and changed the UserDetailsView class and implemented methods with dummy code
"""

class UserDetailsView(Gesture):

  def __init__(self):
    pass

  
  def one_tap(self):
    # open user details view of the user
    # see the name of the user

  
  def double_tap(self):
    # no code in this method as it is not required
    pass
  
  def long_press(self):
    # no code in this method as it is not required
    pass


"""
This is a violation of Single Responsibility method as Class should have single Responsibility
But the UserDetailsView class have multiple responsiblities -> that is not required
it will unintended side effects making the code fragile
"""

"""
Improved code
-> Making seperate interfaces for each type of gesture, then implementing them to classes as required

"""

class SingleTapGesture(abc):

  def __init__(self):
    pass
  
  def one_tap(self):
    pass

class DoubleTapGesture(abc):

  def __init__(self):
    pass
  
  def double_tap(self):
    pass


class LongPressGesture(abc):

  def __init__(self):
    pass
  
  def long_press(self):
    pass


class UserDetailsView(SingleTapGesture):

  def __init__(self):
    pass
  

  def one_tap(self):
    # implement one tap gesture code 



class ProfilePictureView(SingleTapGesture, DoubleTapGesture, LongPressGesture):

  def __init__(self):
    pass
  

  def one_tap(self):
    # implement one tap gesture code 
  
  def double_tap(self):
    # implement double tap gesture code

  
  def long_press(self):
    # implement long press gesture code
