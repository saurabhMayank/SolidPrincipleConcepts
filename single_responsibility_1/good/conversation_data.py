from net_api_core import NetApiCore
from conversation_factory import ConversationFactory
from core_data import CoreData



class ConversationData:
    """
     Responsibility of the class
     Get all the conversations
     Acting as a main class calling the other classes
    """
    NET_API_CORE = NetApiCore()
    CONVERSATION_FACTORY = ConversationFactory()
    CORE_DATA = CoreData()


    def get_all_conversations(self):
        json_data = self.NET_API_CORE.request_data_from_API()
        conversations = self.CONVERSATION_FACTORY.parse_and_create_conversations_from(json_data)
        conversations = self.CORE_DATA.save_to_database(conversations)
        return conversations


conversation_data = ConversationData()
print(conversation_data.get_all_conversations())
