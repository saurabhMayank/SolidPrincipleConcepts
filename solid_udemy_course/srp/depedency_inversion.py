"""
High level modules should not depend on low level modules

Both High Level Modules and Low level modules -> Should depend on abstraction
Notebook has -> Notes in detail

This attribute -> Results in Loose Coupling Between High Level and Low Level modules
"""

# Simple Messaging system
# Low-level module (implementation details)
# Without Depedency Inversion
class EmailService:
    def send_message(self, message):
        print(f"Sending email: {message}")

# High-level module (depends on Low-level module)
class NotificationService:
    def __init__(self):
        self.email_service = EmailService()

    def send_notification(self, message):
        self.email_service.send_message(message)

# Usage
notification_service = NotificationService()
notification_service.send_notification("Hello, World!")

"""
i) `NOTIFICATION SERVICE` -> High Level Module -> Depends on Low Level Module -> Email Service
ii) Both the High Level and Low Level modules are tightly coupled
iii) If there is any change in the low level modules -> Then that change also need to be made in the high level module
For example any change in the email service in terms of parameters or function name change 
Also need to be made in the Notification Service

Notification Service tightly coupled with Email Service -> send notification will only work for email
If in place of Email -> Want to attach SMS service -> Will need to implement new function
(Bad Code Design)

iv) Rigidity, Fragility, Not extensible

"""

# With Depedency Inversion -> Simple Notification System

# Abstraction (interface)
class MessageService(abc):
    @abstract_method
    def send_message(self, message):
        pass

# Low-level module (implementation details)
class EmailService(MessageService):
    def send_message(self, message):
        print(f"Sending email: {message}")

# High-level module (depends on abstraction)
class NotificationService:
    def __init__(self, message_service: MessageService):
        self.message_service = message_service

    def send_notification(self, message):
        self.message_service.send_message(message)

# Usage
email_service = EmailService()
notification_service = NotificationService(email_service)
notification_service.send_notification("Hello, World!")

"""
i) `NotificationService` is dependent on MessageService Interface
ii) EmailService implements MessageService
iii) So here the concept of PollyMorphism is used. Same MessageServiceInterface can have lot of forms
There is EmailService, then there can be SMSService
iv) A form of MessageService can be injected at runtime in the notification service and message can be sent
It can be email service, it can be sms service

-> Solve Rigidity -> Now if EmailService is changed -> it does not affect Notification service
-> Solves Flexibility -> Any MessageService implemented can be injected at run time for sending message

Any change in email service will not randomly break notification service as they are not connected 
to each other

"""

