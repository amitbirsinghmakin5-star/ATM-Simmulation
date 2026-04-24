class ATM:
    def __init__(self, account, transaction):
        self.account = account
        self.transaction = transaction

    def show_balance(self):
        bal = self.account.get_balance()
        self.transaction.add(f"Balance checked: {bal}")
        return bal

    def deposit(self, amount):
        new_bal = self.account.deposit(amount)
        self.transaction.add(f"Deposited: {amount}")
        return new_bal

    def withdraw(self, amount):
        success = self.account.withdraw(amount)

        if success:
            self.transaction.add(f"Withdrawn: {amount}")
            return "Withdrawal Successful"
        else:
            self.transaction.add(f"Failed withdrawal: {amount}")
            return "Insufficient Balance"

    def get_statement(self):
        return self.transaction.statement()