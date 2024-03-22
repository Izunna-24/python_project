from decimal import Decimal


class Aza:
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < Decimal(0.00):
            raise ValueError("Invalid balance amount")
        self.__balance = balance

    def __repr__(self):
        return f'Name {self.name} - Balance{self.__balance}'


account_one = Aza('Izu', Decimal(-200))
print(account_one)
