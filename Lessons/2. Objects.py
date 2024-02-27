class Account:
    def __init__(self, account_number, account_type, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited {amount}")
            print(f"New Balance is: {self.balance}")
        else:
            print(f"{amount} is an invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrawal: {amount}")
            print(f"New Balance: {self.balance}")
        else:
            if amount < 0:
                print(f"{amount} is and invalid amount")
            else:
                print("Insufficient funds")
                print(f"Current balance is {self.balance}")


myaccount = Account(4049, "Savings", 1000)
print(myaccount.account_number)
print(myaccount.account_type)
print(myaccount.balance)
print(myaccount.deposit(100))
