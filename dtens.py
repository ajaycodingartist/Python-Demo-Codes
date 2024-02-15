class BankAccount:
    def __init__(self, account_holder, balance):
        # Private attribute (denoted by a leading double underscore)
        self.__account_holder = account_holder
        # Protected attribute (denoted by a leading single underscore)
        self._balance = balance

    # Public method to get the account holder's name
    def get_account_holder(self):
        return self.__account_holder

    # Public method to get the balance
    def get_balance(self):
        return self._balance
     
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount 
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

# Creating an instance of the BankAccount class
account = BankAccount("John Doe", 1000)

# Accessing public methods to interact with the object
print(f"Account Holder: {account.get_account_holder()}")
print(f"Initial Balance: ${account.get_balance()}")

account.deposit(500)
account.withdraw(200)

# Attempting to access private attribute directly (will raise an AttributeError)
print(account.__account_holder)
 