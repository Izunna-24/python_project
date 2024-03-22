import sys
from datetime import time

from bank_project.bank import Bank
from bank_project.account import Account


class BankApp:
    def __init__(self):
        self.lofty_trust = Bank("Lofty Trust Financials")
        self.banks = []

    def main(self):
        self.use_app()

    def use_app(self):
        print("Welcome to Lofty Trust Financials.")
        self.create_other_banks()

    def create_other_banks(self):
        kuda = Bank("Kuda Bank Inc")
        palmpay = Bank("Palmpay Bank Inc")
        self.banks.append(kuda)
        self.banks.append(palmpay)

        choice = input("Would you like to create an account? [y/n]:\n").lower()
        if choice == "y":
            self.register_customer()
        else:
            self.login()

    def go_to_main_menu(self, account: Account):
        main_menu = """
            Welcome back, what do you want to do today?

            1. Create New Account
            2. Check Balance
            3. Deposit
            4. Transfer
            5. Withdraw
            6. Close Account
            7. Exit App

            Enter a number for option: """

        user_choice = input(main_menu)

        match user_choice:
            case "1":
                self.register_customer()
            case "2":
                self.check_balance(account)
            case "3":
                self.deposit(account)
            case "4":
                self.transfer(account)
            case "5":
                self.withdraw(account)
            case "6":
                self.remove_account(account)
            case "7":
                self.exit_app()
            case _:
                self.go_to_main_menu(account)

    @staticmethod
    def input(prompt):
        return input(prompt)

    def register_customer(self):
        print("To create an account with us, kindly provide your details")

        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter pin: ")

        my_account = self.lofty_trust.register_customer(first_name, last_name, pin)
        print("Account successfully created.")
        print(f"Your account number is {my_account.get_number()}")

        self.login()

    def check_balance(self, account: Account):
        pin = input("Enter account's pin: ")

        try:
            balance = self.lofty_trust.check_balance(account.get_number(), pin)
            print(f"{account.get_name()} balance: ${balance}")
        except Exception as e:
            print(e)
        finally:
            self.go_to_main_menu(account)

    def deposit(self, account: Account):
        amount = input("Enter amount to deposit: ")

        try:
            self.lofty_trust.deposit(account.get_number(), int(amount))
            print("Transaction successful")
        except Exception as e:
            print(e)
        finally:
            self.go_to_main_menu(account)

    def transfer(self, account_number: Account):
        sender_account = input("Enter account number to transfer: ")
        amount = input("Enter amount to transfer: ")
        pin = input("Enter your pin: ")

        try:
            self.lofty_trust.transfer(account_number.get_number(), sender_account, amount, pin)
            print("sent successfully")
        except Exception as e:
            print(e)
        finally:
            self.go_to_main_menu(account_number)

    def withdraw(self, account: Account):
        amount = input("Enter amount to withdraw: ")
        pin = input("Enter your pin: ")

        try:
            self.lofty_trust.withdraw(account.get_number(), int(amount), pin)
            print("Transaction Successful")
        except Exception as e:
            print(e)
        finally:
            self.go_to_main_menu(account)

    @staticmethod
    def print_prompt(prompt):
        print(prompt)

    def remove_account(self, account: Account):
        pin = input("Enter pin: ")

        try:
            self.lofty_trust.remove_account(account.get_number(), pin)
            print("Account removed")
        except Exception as e:
            print(e)
        finally:
            self.go_to_main_menu(account)

    @staticmethod
    def exit_app():
        try:
            print("Closing...")
            time.sleep(2)
            print("Thanks for banking with us")
            sys.exit(0)
        except KeyboardInterrupt:
            print("Thanks for banking with us")

    def login(self):
        print("Enter your login details to continue.")
        account = Account("name", "0000", -1)

        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        try:
            account = self.lofty_trust.find_account(int(account_number))
            if not account.correct_pin(pin):
                print("Invalid pin entered")
                self.login()
        except Exception as e:
            print(e)
            self.register_customer()
        finally:

            self.go_to_main_menu(account)


if __name__ == "__main__":
    app = BankApp()
    app.main()
