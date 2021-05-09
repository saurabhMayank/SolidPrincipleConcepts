"""
Problems with this example is :-
1)Printer class is tightly coupled with book class and formatter class.
2)Printer here prints only book that also only in A4 format because formatter class
denotes the a4 format.
3)So printer class is tightly coupled with book printing in a4 format.
4)If tomorrow I want to print a pamplet in small size,it will not be possible to do that
with this printer class because it directly takes book as an argument and prints it in A4 format.
5) Printer class of this system is immobile, I cannot put this printer in the another system.
"""


class Book:
    """
     Content
    """
    CONTENT = ""
    def __init__(self, content: str):
        self.CONTENT = content

class Formatter:
    """
      Prints the book in only A4 content
    """
    def format(self, book: Book) -> str:
        return book.CONTENT

class Printer:
    """
    Printer Class
    """
    def print(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book

content = "Hey I am coding DI"
book = Book(content)
# print("----book------")
# print(book.CONTENT)
printer = Printer()
print(printer.print(book))