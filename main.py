import json
import datetime
BALANCE = 0
transactions = []

try:
    with open("money_transactions.json", "r") as file_data:
        try:
            transactions = json.load(file_data)
        except json.decoder.JSONDecodeError:
            data = {}
            for transaction in transactions:
                if transaction['type'] == "Income":
                    BALANCE += transaction['amount']
                elif transaction['type'] == "Expense":
                    BALANCE -= transaction['amount']
except FileNotFoundError:
    pass

print("Welcome to Money Tracker App\n")
menu = ["1. Add Income", "2. Add expense", "3. View Balance", "4. View Transaction History", "5. Exit"]
MENU = sorted(menu)
while True:
    for item in MENU:
        print(item)

    prompt = input("Choose what you want to do: ")
    try:
        if prompt < "1" or prompt > "5":
            raise ValueError
        if prompt == "1":
            amount = int(input("Enter your income: "))
            BALANCE += amount
            transaction = {"type": "Income", "amount": amount,
                           "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            transactions.append(transaction)
        elif prompt == "2":
            expense = int(input("Expense amount: "))
            if expense > BALANCE:
                print(f"Insufficient money, your current balance is ${BALANCE}")
            else:
                BALANCE -= expense
                transaction = {"type": "Expense", "amount": expense,
                               "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                transactions.append(transaction)
        elif prompt == "3":
            print(f"New Balance: {BALANCE}")
        elif prompt == "4":
            print("\nTransaction History:")
            for transaction in transactions:
                print(f"{transaction['date']} - {transaction['type']}: ${transaction['amount']}")
        else:
            with open("money_transactions.json", "w") as file_data:
                json.dump(transactions, file_data, indent=4)
            print("Exiting Money Tracker App. Have a great day!")
            break
    except ValueError:
        print("Only integers needed and values between 1 - 5")
