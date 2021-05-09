class ConversionData:
    """
        Gets the array of previous conversation objects
        Responsibilities of this class
        1. Gets the conversation data from the API.
        2. Parse and create conversation objects from API response.
        3. Save the conversation array to Database

        This class has become very rigid, because this class has
        3 reasons to change.

        Modification in 1 method will require testing of
        all the 3 methods and if more methods are added
        to this class, its rigidity will increase

        Single Responisibility Principle states that
        a class should one and only one reason to change
    """

    def request_data_from_API(self) -> dict:
        """
        sends API requests to conversations json data
        """
        json_data = {'1': 'John'}
        return json_data
    
    def parse_and_create_conversations_from(self, data: any) -> list:
        """
        Parse data and create array of conversation dictionaty
        """
        conversation_dict = [{'1': 'John'}]
        return conversation_dict


    def save_to_database(self, conversations: list) -> list:
        """
         saves the data in the database and returns the final data
        """
        return conversations

    def get_all_conversations(self):
        json_data = self.request_data_from_API()
        conversations = self.parse_and_create_conversations_from(json_data)
        conversations = self.save_to_database(conversations)
        