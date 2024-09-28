"""
Concepts about DIP (Dependency Inverstion Principle) and Dependency Injection (DI) written in 
OOPS Implementation Notes copy

Dependency Injection (DI) is a way -> To Implement Dependency Inversion Principle
"""



"""
Old Design
"""
class TextEditor():
    def __init__(self):
        pass

    def check_spelling():
        dict_spell_checker = DictionarySpellChecker()
        dict_spell_checker.check_word()


# DictSpellChecker -> here kept in same module for simplicity
# Ideally it will be different module and impprted here

class DictionarySpellChecker():
    def __init__(self):
        pass
    
    def check_word():
        pass


#-----------------------------------------------------------------

"""
New Design
"""

class TextEditor():
    def __init__(self, spell_checker:SpellChecker):
        self.spell_checker = spell_checker

    def check_spelling():
        spell_checker.check_word()


# SpellChecker interface
# python does not have interface so making abstract class
class SpellChecker(abc):

    def __init__(self):
        pass
    
    @abstractmethod
    def check_word():
        pass

# DictionarySpellChecker concrete class implementing the
# interface
class DictionarySpellChecker(SpellChecker):

    def __init__(self):
        pass
    
    def check_word():
        pass


"""
Loose coupling between DictionarySpellChecker and TextEditor
"""
