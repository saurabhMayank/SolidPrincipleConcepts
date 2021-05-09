# from net_api_core import NetApiCore
# from conversation_factory import ConversationFactory
from core_data import CoreData

class ConversationData:
    """
     Responsibility of the class
     Get all the conversations
     Acting as a main class calling the other classes
     
     This code is perfectly adhering to SRP, then what is the problem with this code.
     Problem with this code is :-
     1) Though it is adhering to the SRP, then also High level Module ConversionData, directly depend on the Low level Module i.e. CoreData
     2) Both these High level Module and low level Module are tightly coupled with each other.
     3) CoreData is a lowlevel Module, that can be easily used in other projects.
     4) But High Level Module CoversionData undeseriably depends on CoreData because of the tight coupling.
     5) USE OF ConversationData 
     ConversationDataController is used in the Messenger App to get the previous conversations json, parse it, and save to Core Data Database, so it can use the previous conversations to display it offline as well in the Messenger App.

     Here the rigidity is that ConversationDataController is designed in such a way thay it does the processing in a way to save the data in the Core Database. (RDS)

     But the Messenger App needs to save the Conversations in the core data base and the Conversations data controller is processing the data in the same way in which the core data database needs it, then what is the issue ??

     The issue is ??
     The functionality of preprocessing of conversion data controller is tightly coupled with core data database.

     Let's say tomorrow there is a requirement to use this Conversation Data Controller into some other APP let's say Intercom where users report issues and we take that conversation and have to save that conversation in something like File System like HDFS

     Then this ConversationDataController will not be able to be used there because of such tight coupling ConversationDataController in other places

     Input data format (RDS)
        MySQL can accept incoming data in one of two forms: flat files and SQL. This section points out some key advantages and disadvantages of each.
     
     Input Format File System Like HDFS( Hadoop Distributed file system)
     Some other format like TextInput format

     Conclusion
     So my point is that undesirable dependecies like this makes the desirable parts of code tightly coupled with undesirable parts of the code, so that it becomes very difficult to seperate the two from each other..
    """
    # NET_API_CORE = NetApiCore()
    # CONVERSATION_FACTORY = ConversationFactory()
    CORE_DATA = CoreData()

    def get_all_conversations(self):
        # json_data = self.NET_API_CORE.request_data_from_API()
        # conversations = self.CONVERSATION_FACTORY.parse_and_create_conversations_from(json_data)

        # also convert the into the required format which is needed by the
        # core data base rds before passing as an argument
        conversations = self.CORE_DATA.save_to_database(conversations)
        return conversations


conversation_data = ConversationData()
print(conversation_data.get_all_conversations())
