class BankAccount(object):
    def __init__(self, bal=0):
        self.balance = bal

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def __str__(self):
        return f"Your current balance is {self.balance:.2f} euro"
