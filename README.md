# bank_account_assignment


For this assignment, don't worry about putting any user information in the BankAccount class.

The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0.

The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantation.

The class should also have the following methods:
    - deposit(self, amount) - increases the account balance by the given amount. 
    - withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insuficient funds: Charging a $5 fee" and deduct $5
    - display_account_info(self) - print to the songole: eg. "Balance: $100"
    - yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
