from abc import ABC,abstractmethod

"""
Problems with this class design structure ??
1. Orcs is a child of middle earth inhabitants abstract class so it should 
perform all the funtionalities of middle earth inhabitants class.
2. But orcs cannot perform dance functionality, this can cause unnecessary
bugs and produce fragility in the code.
Because as orc is a middle earth inhabitant it should inherit from middle earth
inhabitant class but it cannot dance so there is a bug that is caused because of
the violation of the LSP.
"""

class MiddleEarthInhabitant(ABC):
    """
     Abstract class for all the Middle Earth Inhabitants
     Also traits of all the middle earth inhabitants are defined
     In terms of abstract methods
    """
    @abstractmethod
    def dance(self):
        pass

class Human(MiddleEarthInhabitant):
    """
    Humans are child of MiddleEarthInhabitants
    They can dance
    """
    def dance(self):
        print("Going wild on the dance floor.")

class Hobbit(MiddleEarthInhabitant):
    """
     Hobbits are child of MiddleEarthInhabitants
     They can dance
    """
    def dance(self):
        print("Look at those big feet go.")

class Orcs(MiddleEarthInhabitant):
    """
     Orcs are child of Middle Earth Inhabitants
     But they cannot dance
    """

    def dance(self):
        raise NameError('This attribute is not found in orcs')

class Party:
    def __init__(self, guests):
        self._guests = guests

    def que_music(self):
        for guest in self._guests:
            guest.dance()


human = Human()
hobbit = Hobbit()
party = Party([human,hobbit])
print(party.que_music())
#-------------------------------------------
# orcs = Orcs()
# party_new = Party([orcs])
# print(party_new.que_music())