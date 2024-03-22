from decimal import Decimal


class Account:
    def __init__(self, name: str, balance: Decimal):
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= Decimal(0.00):
            raise ValueError("amount must be greater than zero")
        self.__balance += amount

    def withdraw(self, amount):
        pass


a1 = Account("John", Decimal(-1000))
a1.deposit = -1000
print(a1.deposit)


