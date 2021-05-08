from abc import ABC, abstractmethod
class Shape(ABC):
    """
     Abstract class shape having signature of method
     Abstract methods have declaration but they do not have implementation.
     
     This helps to enforce a class to have certain methods so that the
     developer inheriting the class should implement those methods in their child
     classes.
    """
    @abstractmethod
    def area(self):
        pass