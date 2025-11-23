expenses = []   # This will store all expenses as a list of dictionaries

def add_expense():
    print("\n--- Add Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    for i, e in enumerate(expenses, start=1):
        print(f"{i}. Date: {e['date']}, Amount: {e['amount']}, Category: {e['category']}, Description: {e['description']}")


def delete_expense():
    print("\n--- Delete Expense ---")
    view_expenses()
    if not expenses:
        return

    num = int(input("Enter the expense number to delete: "))
    if 1 <= num <= len(expenses):
        expenses.pop(num - 1)
        print("Expense deleted!")
    else:
        print("Invalid number.")


def monthly_total():
    print("\n--- Monthly Total ---")
    month = input("Enter month (YYYY-MM): ")

    total = 0
    for e in expenses:
        if e["date"].startswith(month):
            total += e["amount"]

    print("Total expenses in", month, "=", total)


def main():
    while True:
        print("\n===== Student Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Monthly Total")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            monthly_total()
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main()
