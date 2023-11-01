class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance =  balance


    def deposit(self, amount):
        self.balance += amount
        print(f"Your balance is {self.balance}")
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insuficient funds. ${self.balance}")
        else:
            self.balance -= amount
            print(f"You've withdrawn: ${amount}. You're new balance is: ${self.balance}")

    def display_account_info(self):
        print(f"interest rate: {self.int_rate}")
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        pass