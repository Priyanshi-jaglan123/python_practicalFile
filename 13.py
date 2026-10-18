class BankAccount:
    def __init__(self, account_no, balance):
        self.__account_no = account_no
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Number:", self.__account_no)
        print("Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.get_balance() * rate / 100
        self.deposit(interest)
        print("Interest added:", interest)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.get_balance() + 5000:
            # Allows overdraft up to 5000
            super().withdraw(amount)
        else:
            print("Overdraft limit exceeded.")


# Savings account
print("----- Savings Account -----")

savings = SavingsAccount("S101", 10000)

savings.display()
savings.deposit(2000)
savings.withdraw(1000)
savings.add_interest(5)

savings.display()


# Current account
print("\n----- Current Account -----")

current = CurrentAccount("C101", 5000)

current.display()
current.deposit(3000)
current.withdraw(7000)

current.display()