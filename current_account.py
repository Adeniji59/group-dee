from Account import Account


class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)


current_account = CurrentAccount()
current_account.deposit(500)
current_account.get_balance()
