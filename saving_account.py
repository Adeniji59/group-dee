from Account import Account


class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)
        self.limit = 5000

    def withdraw(self, amount):
        if self.Account_balance - amount < self.limit:
            print("Withdrawal amount exceeds account limit!")
        else:
            self.Account_balance -= amount


saving_account = SavingsAccount()
saving_account.withdraw(200)
saving_account.get_balance()
