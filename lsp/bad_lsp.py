from abc import ABC,abstractmethod

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


# human = Human()
# hobbit = Hobbit()
# party = Party([human, hobbit])
# print(party.que_music())
#-------------------------------------------
# orcs = Orcs()
# party_new = Party([orcs])
# print(party_new.que_music())