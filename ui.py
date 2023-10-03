from tkinter import *
from oop import MoneyTracker
from tkinter import messagebox

window = Tk()
window.title("MONEY TRACKER APP")
window.minsize(width=400, height=300)

money_tracker = MoneyTracker()


def update_total_income_label(total_income):
    transaction_history.delete(END)  # Remove the previous total income entry
    transaction_history.insert(END, f"Total Income: ${total_income}")


def income():
    try:
        money_tracker.add_income(int(income_entry.get()))
        if int(income_entry.get()) < 0:
            raise ValueError
        income_entry.delete(0, END)
        update_transaction_history()
        messagebox.showinfo("Success", "Income added")
        balance_label.config(text=f"Balance: ${money_tracker.balance}")
        update_total_income_label(money_tracker.get_total_income())

    except ValueError:
        messagebox.showerror("Error", "Please enter a positive number")


def expense():
    try:
        money_tracker.add_expenses(int(expense_entry.get()))
        if int(expense_entry.get()) > money_tracker.balance:
            raise ValueError
        expense_entry.delete(0, END)
        update_transaction_history()
        messagebox.showinfo("Success", "Expense added")
        balance_label.config(text=f"Balance: ${money_tracker.balance}")
        update_total_income_label(money_tracker.get_total_income())
    except ValueError:
        messagebox.showerror("Error", "The expense is more than the income")

# income/expense entry that allows the user to enter the income and expense


income_label = Label(window, text="Income:")
income_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
income_entry = Entry(window, width=20)
income_entry.grid(row=1, column=1, padx=10, pady=5)
expense_label = Label(window, text="Expense:")
expense_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
expense_entry = Entry(window, width=20)
expense_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
# income/expense button which when clicked it add both income and expense info
add_income_button = Button(window, text="Add Income", command=income)
add_income_button.grid(row=1, column=2, padx=10, pady=5)

add_expense_button = Button(window, text="Add Expense", command=expense)
add_expense_button.grid(row=2, column=2, padx=10, pady=5)

# A label to display the balance
balance_label = Label(window, text=f"Balance: ${money_tracker.get_balance()}")

balance_label.grid(row=3, column=0, columnspan=2)

# A list box to display transaction history
transaction_history = Listbox(window, width=40, height=10)
transaction_history.grid(row=4, column=0, columnspan=2)

# This is a function that updates the transaction history


def update_transaction_history():
    transaction_history.delete(0, END)
    total_income = 0
    for transaction in money_tracker.transactions:
        transaction_history.insert(END, f"{transaction['date']} - {transaction['type']}: ${transaction['amount']}")
        if transaction['type'] == 'Expense':
            total_income -= transaction['amount']
    money_tracker.total_income = total_income


update_transaction_history()


def delete_all_transactions():
    result = messagebox.askyesno("Confirmation", "Are you sure you want to delete this transaction?")
    if result:
        selected_transaction_index = transaction_history.curselection()[0]
        deleted_transaction = money_tracker.transactions.pop(selected_transaction_index)
        money_tracker.save_transactions()  # Save changes to the JSON file
        update_transaction_history()  # Update the transaction history display
        money_tracker.view_balance()
        update_transaction_history()


delete_button = Button(window, text="Delete", command=delete_all_transactions)
delete_button.grid(row=4, column=2, columnspan=2)


def exit_app():
    window.destroy()  # Close the Tkinter window


exit_button = Button(window, text="Exit", command=exit_app)
exit_button.grid(row=5, column=0, columnspan=2)


window.mainloop()
