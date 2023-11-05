import decimal

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance =  balance


    def deposit(self, amount):
        self.balance += amount
        print(f"Your balance is {self.balance}")
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insuficient funds. Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
            print(f"You've withdrawn: ${amount}. You're new balance is: ${self.balance}")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self




ivan = BankAccount(0.01)

ivan.yield_interest().display_account_info()