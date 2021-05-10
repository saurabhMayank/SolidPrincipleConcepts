from abc import ABC,abstractmethod
"""
How this class structure solved the problem in bad_lsp.py ?
So Now we seperated the abstract classes into two abstract classes
Inherit only the appropriate abstract class and seperating fat abstract classes
into different abstract classes.

Abiding to the LSP principle prevents us from causing unusual like what we saw in bad.py
"""

class MiddleEarthInhabitant(ABC):
    """
     Abstract class for all the Middle Earth Inhabitants
     Also traits of all the middle earth inhabitants are defined
     In terms of abstract methods
    """
    pass

class Dance(ABC):
    """
     Abstract class for those who can dance
    """
    @abstractmethod
    def dance(self):
        pass

class Fight(ABC):
    """
     Abstract class for those who can fight
    """
    @abstractmethod
    def fight(self):
        pass

class Human(MiddleEarthInhabitant,Dance):
    """
    Humans are child of MiddleEarthInhabitants
    They can dance
    """
    def dance(self):
        print("Going wild on the dance floor.")

class Hobbit(MiddleEarthInhabitant,Dance):
    """
     Hobbits are child of MiddleEarthInhabitants
     They can dance
    """
    def dance(self):
        print("Look at those big feet go.")

class Orcs(MiddleEarthInhabitant, Fight):
    """
     Orcs are child of Middle Earth Inhabitants
     But they cannot dance
    """
    def fight(self):
        print("I can kick and punch")

class Party:
    def __init__(self, guests):
        self._guests = guests
    def que_music(self):
        for guest in self._guests:
            if "dance" in dir(guest):
                guest.dance()

class Fight:
    def __init__(self, guests):
        self._guests = guests
    
    def fight_war(self):
        for guest in self._guests:
            if "fight" in dir(guest):
                guest.fight()


human = Human()
hobbit = Hobbit()
orcs = Orcs()
party = Party([human, hobbit, orcs])
print(party.que_music())
fight = Fight([human, hobbit,orcs])
print(fight.fight_war())
