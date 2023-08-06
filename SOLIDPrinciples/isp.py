from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class RefundProcessor(ABC):
    @abstractmethod
    def process_refund(self, amount):
        pass


class OnlinePaymentProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")

newPayment = OnlinePaymentProcessor()
newPayment.process_payment(300)
newPayment.process_refund(700)

'''
This code follow the Interface Segregatio principle as below :


The provided code follows the Interface Segregation Principle (ISP) by segregating the methods into separate interfaces and allowing classes to implement only the interfaces they need. Here's how it adheres to ISP:

1. **PaymentProcessor Interface:** The `PaymentProcessor` abstract base class defines the `process_payment` method.
 This interface represents the behavior of processing a payment and is used by classes that are responsible for handling payment-related operations.

2. **RefundProcessor Interface:** The `RefundProcessor` abstract base class defines the `process_refund` method.
 This interface represents the behavior of processing a refund and is used by classes that handle refund-related operations.

3. **OnlinePaymentProcessor Class:** The `OnlinePaymentProcessor` class implements both the `PaymentProcessor` and `RefundProcessor` interfaces.
 By doing so, it provides implementations for both payment processing and refund processing.

By segregating the methods into separate interfaces, the code ensures that classes can implement only the interfaces they need. 
In this case, the `OnlinePaymentProcessor` class only implements the methods relevant to its role, which are `process_payment` and `process_refund`.
 This design follows the Interface Segregation Principle, providing a clear and focused interface for each specific functionality. 
 Clients can depend on the relevant interfaces without being forced to implement unnecessary methods they do not require.


'''