from unittest import TestCase

from bank_project.account import Account
from bank_project.insufficient_fund_error import InsufficientFundsError
from bank_project.invalid_amount_error import InvalidAmountError
from bank_project.wrong_pin_error import WrongPinError


class TestAccount(TestCase):
    def test_balance_can_be_checked(self):
        initial_balance = 0
        my_account = Account('dora', 'pin', 1)
        actual_balance = my_account.check_balance('pin')
        self.assertEqual(initial_balance, actual_balance)

    def test_that_wrong_pin_raises_error(self):
        my_account = Account('dora', 'pin', 1)
        my_account.deposit(400)
        with self.assertRaises(WrongPinError):
            my_account.withdraw(200, "l")

    def test_that_money_can_be_deposited(self):
        my_account = Account('dora', 'pin', 1)
        my_account.deposit(100)
        initial_balance = 100
        self.assertEqual(initial_balance, my_account.check_balance('pin'))

    def test_that_invalid_deposit_raises_error(self):
        my_account = Account('dora', 'pin', 1)
        with self.assertRaises(InvalidAmountError):
            my_account.deposit(-5000)

    def test_that_withdraw_can_be_made(self):
        my_account = Account('dora', 'pin', 1)
        my_account.deposit(1200)
        my_account.withdraw(1000, "pin")
        balance = 200
        self.assertEqual(balance, my_account.check_balance('pin'))

    def test_that_withdrawal_above_balance_raises_insufficient_funds_error(self):
        my_account = Account('dora', 'pin', 1)
        my_account.deposit(500)
        with self.assertRaises(InsufficientFundsError):
            my_account.withdraw(1000, "pin")
