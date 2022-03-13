import json
import banking_system as bank


class Account:
    def __init__(self):
        pass

    def admin_data(self):
        try:
            with open("Boris.json") as b:
                boris = json.load(b)

            with open("Chloe.json") as c:
                chloe = json.load(c)

            with open("David.json") as d:
                david = json.load(d)
        except FileNotFoundError:
            print("User files do not exist.")

        return boris, chloe, david

    def load_data(self):
        try:
            if bank.username == "Boris":
                with open("Boris.json") as b:
                    data = json.load(b)
                    return data
            elif bank.username == "Chloe":
                with open("Chloe.json") as c:
                    data = json.load(c)
                    return data
            elif bank.username == "David":
                with open("David.json") as d:
                    data = json.load(d)
                    return data
        except FileNotFoundError:
            print(f"File {bank.username}.json does not exist.")

    def deposit(self, index):
        data = Account.load_data(self)
        try:
            deposit = int(input("How much would you like to deposit: "))
            balance = data["User"]["Accounts"][index]["Balance"]
            new_balance = balance + deposit
            data["User"]["Accounts"][index]["Balance"] = new_balance
        except ValueError:
            print("Invalid amount. Amount has to an integer: e.g 100")
            self.deposit(self, index)

        if bank.username == "Boris":
            with open("Boris.json", "w") as b:
                json.dump(data, b, indent=4)
        elif bank.username == "Chloe":
            with open("Chloe.json", "w") as c:
                json.dump(data, c, indent=4)
        elif bank.username == "David":
            with open("David.json", "w") as d:
                json.dump(data, d, indent=4)

    def withdraw(self, index):
        data = Account.load_data(self)
        try:
            withdraw = int(input("How much would you like to withdraw: "))
        except ValueError:
            print("Invalid amount. Amount has to an integer: e.g 100")
            self.withdraw(self, index)
        try:
            balance = data["User"]["Accounts"][index]["Balance"]
            over_limit = data["User"]["Accounts"][index]["Overdraft limit"]
            overall_balance = balance + over_limit
            if withdraw > overall_balance:
                print("Insufficient funds")
            elif withdraw <= overall_balance:
                temp_balance = overall_balance - withdraw
                new_balance = temp_balance - over_limit
                data["User"]["Accounts"][index]["Balance"] = new_balance

        except KeyError:
            balance = data["User"]["Accounts"][index]["Balance"]
            if withdraw > balance:
                print("Insufficient funds")
            elif withdraw <= balance:
                new_balance = balance - withdraw
                data["User"]["Accounts"][index]["Balance"] = new_balance

        if bank.username == "Boris":
            with open("Boris.json", "w") as b:
                json.dump(data, b, indent=4)
        elif bank.username == "Chloe":
            with open("Chloe.json", "w") as c:
                json.dump(data, c, indent=4)
        elif bank.username == "David":
            with open("David.json", "w") as d:
                json.dump(data, d, indent=4)
