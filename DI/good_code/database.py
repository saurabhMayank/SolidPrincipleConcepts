from abc import ABC, abstractmethod
class Database(ABC):
    """
     Abstract class database defining methods all the different concrete
     DB classes should posses
    """

    @abstractmethod
    def convert_data_to_appopriate_format(self):
        pass
    
    @abstractmethod
    def save_to_database(self):
        pass