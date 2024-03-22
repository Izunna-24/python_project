import random
from bank_project.account_not_found_error import AccountNotFoundError
from bank_project.account import Account


class Bank:
    def __init__(self, name):
        self.accounts = []
        self.name = name

    def number_of_accounts(self):
        return len(self.accounts)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_number() == account_number:
                return account
        return None

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account is None:
            raise AccountNotFoundError("Account not found")
        account.deposit(amount)

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        if account is None:
            raise AccountNotFoundError("Account not found!!")
        return account.check_balance(pin)

    def register_customer(self, first_name, last_name, pin):
        new_account_number = self.generate_account_number()
        name = first_name + " " + last_name
        mandi = Account(name, pin, new_account_number)
        self.accounts.append(mandi)
        return mandi

    @staticmethod
    def generate_account_number():
        new_number = random.randint(100_000_000, 999_999_999)
        return new_number

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        if account is None:
            raise AccountNotFoundError("Account not found!!")
        account.withdraw(amount, pin)

    def transfer(self, from_account_number, to_account_number, amount, pin):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if from_account is None or to_account is None:
            raise AccountNotFoundError("Account not found!!")
        from_account.withdraw(amount, pin)
        to_account.deposit(amount)

    def remove_account(self, account_number, pin: str):
        account = self.find_account(account_number)
        self.accounts.remove(account)
