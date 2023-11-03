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

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        pass



ivan = BankAccount()

ivan.display_account_info()