import json
import accounts as acc
import tkinter as tk
username = ""


class BankingSystem:

    def __init__(self):
        self.admin_login = ["Arthur", "123"]

    def user_login(self):
        global username
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        data = acc.Account.load_data(self)

        try:
            if str(username) in self.admin_login and str(password) in self.admin_login:
                print("Logged in as admin")
                Admin().display_menu()
            elif str(username) in data["User"]["Name"] and str(password) in data["User"]["Password"]:
                print(f"Succesfully logged in. Welcome {username}")
                User().display_menu()
            else:
                print("Invalid username/password.")
                self.user_login()

        except TypeError:
            print("Invalid username/password.")
            self.user_login()

    def run_app(self):
        BankingSystem().user_login()


class User:

    def __init__(self):
        pass

    def display_menu(self):
        print("Please select an option:")
        print("  1 - View account")
        print("  2 - View summary")
        print("  3 - Quit")

        try:
            choice = int(input("Enter a number to select your option: "))
        except ValueError:
            print("Invalid choice. Try again.")
            self.display_menu()

        if choice == 1:
            self.view_account()
        elif choice == 2:
            self.view_summary()
        elif choice == 3:
            print("Goodbye")
        else:
            print("Invalid input. Try again.")
            self.display_menu()

    def view_account(self):
        data = acc.Account.load_data(self)
        id = 1
        index = 0
        accounts = data["User"]["Accounts"]
        print("--Account list--")
        print("Please select an option:")
        for account in accounts:
            account = data["User"]["Accounts"][index]["Type"]
            balance = data["User"]["Accounts"][index]["Balance"]
            print(f"  {id} - {account}: £{balance}")
            id += 1
            index += 1
        index = 0
        try:
            choice = int(input("Enter a number to select your option: "))
            index = choice - 1
            account = data["User"]["Accounts"][index]["Type"]
            balance = data["User"]["Accounts"][index]["Balance"]
        except IndexError:
            print("This account doesn't exist. Please try another one.")
            self.view_account()
        except ValueError:
            print("Invalid choice. Try again.")
            self.view_account()
        print(f"You selected {choice} - {account}: £{balance}")
        print("Please select an option:")
        print("  1 - Deposit")
        print("  2 - Withdraw")
        print("  3 - Go back")

        choice2 = int(input("Enter a number to select your option: "))

        if choice2 == 1:
            acc.Account.deposit(self, index)
            self.view_account()
        elif choice2 == 2:
            acc.Account.withdraw(self, index)
            self.view_account()
        elif choice2 == 3:
            self.view_account()
        else:
            print("Invalid input. Try again.")
            self.view_account()

    def view_summary(self):
        data = acc.Account.load_data(self)
        num_of_accs = 0
        total_bal = 0
        index = 0
        address = data["User"]["Address"]
        accounts = data["User"]["Accounts"]
        for account in accounts:
            account = data["User"]["Accounts"][index]["Type"]
            balance = data["User"]["Accounts"][index]["Balance"]
            num_of_accs += 1
            index += 1
            total_bal += balance
        print("--Account summary--")
        print(f"{num_of_accs} account(s) £{total_bal} in total")
        print(f"Your address: {address}")


class Admin:

    def __init__(self):
        pass

    def display_menu(self):
        print("Please select an option:")
        print("  1 - Customer Summary")
        print("  2 - Financial Forecast")
        print("  3 - Transfer Money - GUI")
        print("  4 - Account management - GUI")

        try:
            choice = int(input("Enter a number to select your option: "))
        except ValueError:
            print("Invalid choice. Try again.")
            self.display_menu()

        if choice == 1:
            self.customer_summary()
        elif choice == 2:
            self.financial_forecast()
        elif choice == 3:
            self.transfer_money()
        elif choice == 4:
            self.account_man()
        else:
            print("Invalid input. Try again.")
            self.display_menu()

    def customer_summary(self):
        user_data = acc.Account.admin_data(self)
        user = 0
        for i in user_data:
            print()
            name = user_data[user]["User"]["Name"]
            address = user_data[user]["User"]["Address"]
            accounts = user_data[user]["User"]["Accounts"]
            print(f"Name: {name}")
            print(f"Address: {address}")
            print("Accounts:")
            index = 0

            for account in accounts:
                try:
                    account = user_data[user]["User"]["Accounts"][index]["Type"]
                    balance = user_data[user]["User"]["Accounts"][index]["Balance"]
                    interest_rate = user_data[user]["User"]["Accounts"][index]["Interest rate"]
                    print(f"{account}: £{balance} Interest rate: {interest_rate}%")
                except KeyError:
                    account = user_data[user]["User"]["Accounts"][index]["Type"]
                    balance = user_data[user]["User"]["Accounts"][index]["Balance"]
                    overdraft = user_data[user]["User"]["Accounts"][index]["Overdraft limit"]
                    print(f"{account}: £{balance} Overdraft limit: £{overdraft}")
                index += 1
            user += 1

    def financial_forecast(self):
        user_data = acc.Account.admin_data(self)
        user = 0
        for i in user_data:
            print()
            name = user_data[user]["User"]["Name"]
            accounts = user_data[user]["User"]["Accounts"]
            print(f"Name: {name}")
            index = 0
            num_of_accs = 0
            total_bal = 0
            int_bal = 0
            forecast_bal = 0

            for account in accounts:
                try:
                    account = user_data[user]["User"]["Accounts"][index]["Type"]
                    balance = user_data[user]["User"]["Accounts"][index]["Balance"]
                    interest_rate = user_data[user]["User"]["Accounts"][index]["Interest rate"]
                    num_of_accs += 1
                    total_bal += balance
                    interest = interest_rate / 100
                    int_bal = balance * interest
                    forecast_bal += int_bal
                    forecast_bal += balance

                except KeyError:
                    account = user_data[user]["User"]["Accounts"][index]["Type"]
                    balance = user_data[user]["User"]["Accounts"][index]["Balance"]
                    overdraft = user_data[user]["User"]["Accounts"][index]["Overdraft limit"]
                    num_of_accs += 1
                    total_bal += balance
                    forecast_bal += balance
                index += 1
            print(f"Number of accounts: {num_of_accs}")
            print(f"Total balance: {total_bal}")
            print(f"Forecast of total balance: {forecast_bal:.2f}")
            user += 1

    def transfer_money(self):
        main_window = tk.Tk()
        main_window.title("Transfer money")

        label = tk.Label(text="please choose customer: ")
        entry = tk.Entry()
        button1 = tk.Button(text="next")
        button2 = tk.Button(text="back", command=main_window.destroy)

        label.pack()
        entry.pack()
        button1.pack()
        button2.pack()

        main_window.mainloop()

    def account_man(self):
        main_window = tk.Tk()
        main_window.title("Account management")

        label = tk.Label(text="please choose customer: ")
        entry = tk.Entry()
        button1 = tk.Button(text="next")
        button2 = tk.Button(text="back", command=main_window.destroy)

        label.pack()
        entry.pack()
        button1.pack()
        button2.pack()

        main_window.mainloop()
