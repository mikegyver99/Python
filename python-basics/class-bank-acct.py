# The Goal: Create a class named BankAccount.
# It should initialize with an owner and a balance.
# Add a method deposit(amount).
# Add a method withdraw(amount) that only succeeds if 
# there are sufficient funds; otherwise, it should print "Insufficient funds."

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")
# Example usage:
account = BankAccount("Alice", 100)
account.deposit(50)
print(account.balance)  # Output: 150
account.withdraw(30)
print(account.balance)  # Output: 120
account.withdraw(200)  # Output: Insufficient funds.
