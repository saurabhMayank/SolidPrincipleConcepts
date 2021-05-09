class CoreData:
    """
     Responsibility of the class
     Save Data to the Core DB (RDS)
    """
    def save_to_database(self, conversations: list) -> list:
        """
         saves the data in the database and returns the final data
        """
        return conversations