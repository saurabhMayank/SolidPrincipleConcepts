from abc import ABC, abstractmethod

"""
How the class solves the problems mentioned in bad.py class ?
1. Fat Interface(abstract class) broken into different interfaces(abstract class).
2. Concrete class inherits only those abstract classes that it requries.
3. Probability of creating unnecessary bugs is not there anymore.
"""

class TapGesture(ABC):
    """
    Abstract Class defining methods of tap gesture
    """
    @abstractmethod
    def did_tap():
        pass
    
class DoubleTap(ABC):
    """
    Double Tap Class defining methods of double tap
    """

    @abstractmethod
      def did_double_tap():
        pass

class LongTap(ABC):
    """
    Long tap class defining methods of Long Press feature
    """

    @abstractmethod
    def did_long_tap():
        pass

class UserDetailView(TapGesture,DoubleTap,LongTap):
      """
        Inherits all the three abstract class
        Gives the feature to view the image in a profile using different gestures
        In a social media app
        The methods defined in the defined in the different abstract class
        can be implemented in this concrete class
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

class UserDetailView(TapGesture):
    """
     Inherits only the abstract class that is needed because in user detail view
     only tap feature will work rest other features won't work..
     This reduces probability of lot of bugs because unnecessary method implementations
     are not needed
    """
    def did_tap():
        # did tap functionality implemented
        pass