# Fix the Errors
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self ,amount):
        if amount > 0:
            self.__balance += amount  # Error here
        else:
            print("Deposit must be greater than zero")

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount  # Error here
        else:
            print("❌ Not enough balance!")
    @property
    def balance(self):
        return self.__balance  # Error here

# Testing
acc = BankAccount("Ali", 1000)
acc.deposit(500)
print(acc.balance())  # Expected Output: 1500
acc.withdraw(2000)  # Expected Output: ❌ Not enough balance!
print(acc.balance)  # ❌ This should not be directly accessible!
