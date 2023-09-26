import json
import datetime


class MoneyTracker:
    def __init__(self, file_path="money_transactions.json"):
        # Attributes
        self.balance = 0
        self.transactions = []
        self.file_path = file_path
        self.load_transactions()

    def load_transactions(self):
        try:
            with open(self.file_path, "r") as file_data:
                try:
                    self.transactions = json.load(file_data)
                except json.decoder.JSONDecodeError:
                    self.transactions = {}
                    for transaction in self.transactions:
                        if transaction['type'] == "Income":
                            self.balance += transaction['amount']
                        elif transaction['type'] == "Expense":
                            self.balance -= transaction['amount']
        except FileNotFoundError:
            pass

    def add_income(self, amount):
        self.balance += amount
        transaction = {"type": "Income", "amount": amount,
                       "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        self.transactions.append(transaction)
        self.save_transactions()

    def add_expenses(self, amount):
        if amount > self.balance:
            print(f"Insufficient money, your current balance is ${self.balance}")
        elif amount < 0:
            print("Only positive digits")
            raise ValueError

        else:
            self.balance -= amount
            transaction = {"type": "Expense", "amount": amount,
                           "date": self.format_date()}
            self.transactions.append(transaction)
            self.save_transactions()

    def view_balance(self):
        print(f"New Balance is: ${self.balance}")

    def save_transactions(self):
        with open(self.file_path, "w") as file_data:
            json.dump(self.transactions, file_data, indent=4, sort_keys=True)

    def format_date(self):
        return datetime.datetime.now().strftime("%Y-%m-d %H:%M:%S")

    def start_app(self):
        print("Welcome to Money Tracker App")
        while True:
            print("\nMenu:")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Balance")
            print("4. Exit")

            user_input = input("Choose from the menu above: ")
            if user_input == "1":
                amount = int(input("Enter your income: "))
                self.add_income(amount)
            elif user_input == "2":
                amount = int(input("Enter your expense: "))
                self.add_expenses(amount)
            elif user_input == "3":
                self.view_balance()
            elif user_input == "4":
                print("Exiting Money Tracker App. Have a great day!")
                break
            else:
                print("Exiting Money Tracker App. Have a great day!")
                break


money_tracker = MoneyTracker()
money_tracker.start_app()

