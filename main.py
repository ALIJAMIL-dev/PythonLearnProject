class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Fixed: Now correctly updates balance
        else:
            print("Deposit must be greater than zero")

    def withdraw(self, amount):
        if amount <= self.__balance:  # Fixed: Condition should be <= instead of <
            self.__balance -= amount  # Fixed: Used -= to subtract the amount
        else:
            print("❌ Not enough balance!")

    @property  # Added @property to use balance as an attribute
    def balance(self):
        return self.__balance  # Fixed: Now returns the correct value

# Testing
acc = BankAccount("Ali", 1000)
acc.deposit(500)
print(acc.balance)  # ✅ Output: 1500 (No parentheses needed)

acc.withdraw(2000)  # ✅ Output: ❌ Not enough balance!
print(acc.balance)  # ✅ Output: 1500

# Trying to access private variable directly (should not work)
# print(acc.__balance)  # ❌ AttributeError (Cannot access private attributes)
