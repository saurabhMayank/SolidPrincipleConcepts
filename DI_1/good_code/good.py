from abc import ABC, abstractmethod

"""
How this class structure overcomes the  problems bad.py has
1.
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

