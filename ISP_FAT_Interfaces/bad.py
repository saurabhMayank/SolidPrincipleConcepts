from abc import ABC, abstractmethod

"""
Problems with this class design is 
1. Gesture abstract class has lot of methods.
2. Different Concrete classes inherit the abstract concrete class.
3. Some classes concrete do not need all the methods of the Gesture abstract class
but they will have to anyway define it.
This will cause unnecessary bugs and make the code fragile.
"""

class Gesture(ABC):
    """
     Class signifying different gestures
    """
    @abstractmethod
    def did_tap():
        pass
    @abstractmethod
    def did_double_tap():
        pass
    @abstractmethod
    def did_long_tap():
        pass

class ProfileImageView(Gesture):
    """
     Inherits the gesture abstract class
     Gives the feature to view the image in a profile using different gestures
     In a social media app
     All the gestures defined in Gesture abstract class
     Can be implemented by the ProfileImageView concrete class
    """
    def did_tap():
        # did tap functionality implemented
        pass
    def did_double_tap():
        # did double tap functionality implemented
        pass
    def did_long_tap():
        # did long tap funtionality implemented
        pass

class UserDetailView(Gesture):
    """
    Inherits the Gesture abstract class 
    All the Gestures methods cannot implemented here because simply there is
    no use of them in user detail view feature
    """

    def did_tap():
         # did tap functionality implemented
        pass

    def did_double_tap():
        # not implemented left blank
        # as this functionality is not simply there in user detail view
        # double tap is used to give heart emoji but in user detail view there is no
        # functionality for giving heart emoji
        pass

    def did_long_tap():
        # not implemented left blank
        # as this functionality is not simply there in user detail view
        # long tap is used to comment on the picture but in user detail view
        # there is no functionality to comment
        pass


