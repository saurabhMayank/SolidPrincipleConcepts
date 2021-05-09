from abc import ABC, abstractmethod

"""
How this class structure overcomes the  problems bad.py has
1.This class structure has Low level modules implement the abstract classes.
2.This class structure has High Level Module having source code dependency with the
abstract classes.
3.So the Printer class is not tightly coupled now with low level modules book and a4formatter.
4.Printer from this system can be easily plugged out and put into any other system.

SO this is an example of Dependency Inversion. Because of Inverting the Source code dependency 
the problem immobility of modules in the system is solved now.
"""

class HasContent(ABC):
    CONTENT: str


class Book(HasContent):
    CONTENT = ""
    def __init__(self, content):
        self.CONTENT = content


class Formatter(ABC):
    @abstractmethod
    def format(self, has_content: HasContent):
        pass

class A4Formatter(Formatter):
    def format(self, has_content: HasContent):
        """
        This class should obviously contain logic to format to A4 size.
        """
        return has_content.CONTENT

class Printer:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter

    def print(self, has_content: HasContent):
        formatted_book = self.formatter.format(has_content)
        return formatted_book


a4_formatter = A4Formatter()
content = "Hey I am coding DI in a pretty good way"
book = Book(content)
printer = Printer(a4_formatter)
print(printer.print(book))

