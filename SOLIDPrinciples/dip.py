from abc import ABC, abstractmethod

# Abstraction for the email sending functionality
class EmailSender(ABC):
    @abstractmethod
    def send_email(self, recipient, subject, message):
        pass

# Concrete implementation of EmailSender
class ConcreteEmailSender(EmailSender):
    def send_email(self, recipient, subject, message):
        print(f"Sending email to {recipient}: {subject} - {message}")

# NotificationService depends on the EmailSender abstraction
class NotificationService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def send_notification(self, recipient, message):
        self.email_sender.send_email(recipient, "Notification", message)

# Using the NotificationService with a concrete implementation of EmailSender
email_sender = ConcreteEmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification("user@example.com", "Hello, this is a notification!")


'''

The provided code follows the Dependency Inversion Principle (DIP) by relying on abstractions rather than concrete implementations. Let's see how it adheres to DIP:

1. **EmailSender Abstraction (Dependency):** The `EmailSender` abstract base class serves as an abstraction for the email sending functionality. 
It defines the `send_email` method, which represents the behavior of sending an email. By using an abstract base class,
we create a contract that any concrete implementation of `EmailSender` must adhere to.
This abstraction allows the `NotificationService` to depend on the email sending functionality without being tightly coupled to any specific implementation.

2. **ConcreteEmailSender (Implementation):** The `ConcreteEmailSender` class is a concrete implementation of the `EmailSender` abstraction.
 It provides a specific implementation for the `send_email` method. In this example, it prints the email details to the console. However, this implementation could be swapped with any other implementation of `EmailSender` without affecting the `NotificationService` class. The `NotificationService` doesn't need to know the internal details of the implementation; it only relies on the abstraction.

3. **NotificationService (High-Level Module):** The `NotificationService` class is a high-level module that provides the functionality of sending notifications. 
It depends on the `EmailSender` abstraction. By accepting an instance of `EmailSender` through its constructor (`__init__`), the `NotificationService` class can work with any implementation of `EmailSender`. This constructor injection allows the `NotificationService` class to be decoupled from specific implementations of the email sending functionality.

By relying on abstractions (the `EmailSender` abstract base class) and accepting dependencies through constructor injection, the `NotificationService` class adheres to the Dependency Inversion Principle. It is not directly dependent on concrete implementations of the email sending functionality, allowing for flexibility, extensibility, and easy swapping of implementations without modifying the `NotificationService` class itself.



'''