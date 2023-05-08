class Account:
    name = "Ayomide_Oyewole"
    Account_number = 9160609954
    Account_Balance = 10000

    def __init__(self):
        self.name = "Ayomide_Oyewole"
        self.Account_number = 9160609954
        self.Account_balance = 10000

    def deposit(self, amount):
        self.Account_balance += amount
        print("deposit_successful")

    def withdrawal(self, amount):
        self.Account_balance -= amount
        print("withdrawal_successful")

    def get_balance(self):
        print(self.Account_balance)
