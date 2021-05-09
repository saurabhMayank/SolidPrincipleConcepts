from database import Database
class CoreData(Database):
    """
     Responsibility of the class.
     It implements the two methods defined in the 
     abstract class.
     Convert the data into appropriate format
     Save Data to the Core DB (RDS)
    """

    def convert_data_to_appopriate_format(self, conversations):
        """
        converts the data into appropriate format needed by the
        core db
        """
        return conversations
    
    def save_to_database(self, conversations: list) -> list:
        """
         saves the data in the database and returns the final data
        """
        return conversations