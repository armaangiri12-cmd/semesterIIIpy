# Demonstrates creating an account and using deposit and withdrawal methods.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrew:", amount)

    def display_balance(self):
        print(self.owner + "'s balance:", format(self.balance, ".2f"))


account = BankAccount("Aarav", 1000)
account.deposit(500)
account.withdraw(200)
account.display_balance()
