class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute (encapsulated)
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount should be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("Alice")
account.deposit(100)
print("Current balance:", account.get_balance())
account.withdraw(50)
print("Updated balance:", account.get_balance())

print(account.account_holder)
# Trying to access the private attribute directly will cause an error
# print(account.__balance) # This will raise an AttributeError
