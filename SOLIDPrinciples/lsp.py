from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Remaining balance: ${self.balance}")

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds!")

class CheckingAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        available_balance = self.balance + self.overdraft_limit
        if amount <= available_balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account):
    account.deposit(1000)
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)

if __name__ == "__main__":
    # Creating instances of SavingsAccount and CheckingAccount
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    # Performing actions on both accounts
    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)




'''
How this follow the loskov;s substitution princile :

we created the BankAccount abstract base class that defines the common behavior for both SavingsAccount and CheckingAccount,
including the deposit method. The withdraw method is declared as an abstract method in the BankAccount,
which means any subclass inheriting from it must override this method. This enforces that both subclasses will have a withdraw method, 
but the specific implementation in CheckingAccount allows overdrafts while adhering to the expected behavior of a bank account. 
This design follows the Liskov Substitution Principle by ensuring that objects of the superclass can be replaced by objects of
their subclasses without affecting the program's correctness.
'''