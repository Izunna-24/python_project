from bank_project.insufficient_fund_error import InsufficientFundsError
from bank_project.invalid_amount_error import InvalidAmountError
from bank_project.wrong_pin_error import WrongPinError


class Account:
    def __init__(self, name: str, pin: str, number: int):
        self._pin = pin
        self._balance = 0
        self.name = name
        self._number = number

    def is_correct(self):
        return self._pin

    def validate_pin(self, pin):
        if self._pin != pin:
            raise WrongPinError("Wrong Pin")

    def check_balance(self, pin):
        self.validate_pin(pin)
        return self._balance

    def deposit(self, amount: int):
        self.validate_amount(amount)
        self._balance += amount

    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            raise InvalidAmountError("Invalid amount")

    def withdraw(self, withdrawal_amount, pin):
        self.validate_pin(pin)
        self.validate_amount(withdrawal_amount)
        if withdrawal_amount > self._balance:
            raise InsufficientFundsError("Invalid amount")
        self._balance -= withdrawal_amount

    def get_number(self):
        return self._number

    def correct_pin(self, pin):
        return self._pin == pin

    def get_name(self):
        return self.name
