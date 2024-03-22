from unittest import TestCase

from bank_project.bank import Bank


class BankTest(TestCase):
    def setUp(self):
        self.my_bank = Bank('Lofty Trust Financials')

    def test_that_customer_can_be_registered_in_bank(self):
        self.my_bank.register_customer("firstName", "lastName", "Pin")
        self.assertEqual(1, self.my_bank.number_of_accounts())

    def test_that_deposit_can_be_made_in_bank(self):
        peter = self.my_bank.register_customer("firstName", "lastName", "Pin")
        new_account_number = peter.get_number()
        self.assertEqual(0, peter.check_balance("Pin"))
        self.my_bank.deposit(new_account_number, 2000)
        self.assertEqual(2000, self.my_bank.check_balance(new_account_number, "Pin"))

    def test_money_is_in_bank_withdrawal_can_be_made(self):
        account = self.my_bank.register_customer("Drew", "Black", "pin")
        new_account_number = account.get_number()
        self.assertEqual(0, account.check_balance("pin"))
        self.my_bank.deposit(new_account_number, 5000)
        self.assertEqual(5000, account.check_balance("pin"))
        self.my_bank.withdraw(new_account_number, 2000, "pin")
        self.assertEqual(3000, account.check_balance("pin"))

    def test_balance_can_be_checked_in_bank(self):
        account = self.my_bank.register_customer("Drew", "Black", 'pin')
        account_number = account.get_number()
        self.my_bank.check_balance(account_number, 'pin')
        self.assertEqual(0, self.my_bank.check_balance(account_number, 'pin'))

    def test_that_money_is_in_bank_and_transfer_can_be_made_from_one_account_to_another_account(self):
        account = self.my_bank.register_customer("Black", "Drew", "Pin")
        from_account_number = account.get_number()
        self.my_bank.deposit(from_account_number, 2000)
        self.assertEqual(2000, self.my_bank.check_balance(from_account_number, "Pin"))
        self.my_bank.withdraw(from_account_number, 1000, "Pin")
        to_account_number = account.get_number()
        self.my_bank.transfer(from_account_number, to_account_number, 1000, "Pin")
        self.assertEqual(1000, self.my_bank.check_balance(to_account_number, "Pin"))
