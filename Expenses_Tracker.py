import json
from datetime import datetime


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

            for expense in expenses:
                if "date" not in expense:
                    expense["date"] = "Not available"

            return expenses

    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def get_date():
    while True:
        date = input("Enter date (DD-MM-YYYY): ")

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date
        except ValueError:
            print("Please enter a valid date.")


def add_expense(expenses):
    category = input("Enter category: ")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")

    description = input("Enter description: ")
    date = get_date()

    expense = {
        "category": category,
        "amount": amount,
        "description": description,
        "date": date
    }

    expenses.append(expense)

    print("\nExpense added successfully!")


def view_expenses(expenses):
    print("\n===== All Expenses =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print("\nExpense", i)
        print("Category:", expense["category"])
        print("Amount: ₹", expense["amount"])
        print("Description:", expense["description"])
        print("Date:", expense.get("date", "Not available"))


def calculate_total(expenses):
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Amount Spent: ₹", total)


def find_highest(expenses):
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    highest_expense = None

    for expense in expenses:
        if highest_expense is None or expense["amount"] > highest_expense["amount"]:
            highest_expense = expense

    print("\n===== Highest Expense =====")
    print("Category:", highest_expense["category"])
    print("Amount: ₹", highest_expense["amount"])
    print("Description:", highest_expense["description"])
    print("Date:", highest_expense.get("date", "Not available"))


def find_lowest(expenses):
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    lowest_expense = None

    for expense in expenses:
        if lowest_expense is None or expense["amount"] < lowest_expense["amount"]:
            lowest_expense = expense

    print("\n===== Lowest Expense =====")
    print("Category:", lowest_expense["category"])
    print("Amount: ₹", lowest_expense["amount"])
    print("Description:", lowest_expense["description"])
    print("Date:", lowest_expense.get("date", "Not available"))


def search_expense(expenses):
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    search_category = input("\nEnter category to search: ")

    found = False

    print("\n===== Search Results =====")

    for expense in expenses:
        if expense["category"].lower() == search_category.lower():
            print("Category:", expense["category"])
            print("Amount: ₹", expense["amount"])
            print("Description:", expense["description"])
            print("Date:", expense.get("date", "Not available"))
            print()
            found = True

    if found == False:
        print("No expenses found for this category.")


def delete_expense(expenses):
    print("\n===== Delete Expense =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            i,
            ".",
            expense["category"],
            "₹",
            expense["amount"],
            "|",
            expense.get("date", "Not available")
        )

    while True:
        try:
            delete_number = int(input("\nEnter expense number to delete: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    delete_index = delete_number - 1

    if 0 <= delete_index < len(expenses):
        deleted_expense = expenses.pop(delete_index)

        print("\nExpense deleted successfully!")
        print(
            "Deleted:",
            deleted_expense["category"],
            "₹",
            deleted_expense["amount"]
        )
    else:
        print("\nInvalid expense number.")


def update_expense(expenses):
    print("\n===== Update Expense =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            i,
            ".",
            expense["category"],
            "₹",
            expense["amount"],
            "|",
            expense.get("date", "Not available")
        )

    while True:
        try:
            update_number = int(input("\nEnter expense number to update: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    update_index = update_number - 1

    if 0 <= update_index < len(expenses):
        new_category = input("Enter new category: ")

        while True:
            try:
                new_amount = float(input("Enter new amount: "))

                if new_amount < 0:
                    print("Amount cannot be negative.")
                    continue

                break

            except ValueError:
                print("Please enter a valid amount.")

        new_description = input("Enter new description: ")
        new_date = get_date()

        expenses[update_index]["category"] = new_category
        expenses[update_index]["amount"] = new_amount
        expenses[update_index]["description"] = new_description
        expenses[update_index]["date"] = new_date

        print("\nExpense updated successfully!")

    else:
        print("\nInvalid expense number.")


def monthly_expense(expenses):
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    while True:
        month = input("\nEnter month (MM-YYYY): ")

        try:
            datetime.strptime(month, "%m-%Y")
            break
        except ValueError:
            print("Please enter a valid month.")

    found = False
    total = 0

    print("\n===== Monthly Expenses =====")

    for expense in expenses:
        date = expense.get("date", "")

        if date != "Not available" and len(date) == 10:
            expense_month = date[3:]

            if expense_month == month:
                print("\nCategory:", expense["category"])
                print("Amount: ₹", expense["amount"])
                print("Description:", expense["description"])
                print("Date:", date)

                total = total + expense["amount"]
                found = True

    if found == False:
        print("No expenses found for", month)
    else:
        print("\nTotal for", month, ": ₹", total)


def category_summary(expenses):
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] = category_totals[category] + amount
        else:
            category_totals[category] = amount

    print("\n===== Category-wise Summary =====")

    for category, total in category_totals.items():
        print(category, ": ₹", total)


expenses = load_expenses()

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Amount")
    print("4. Highest Expense")
    print("5. Lowest Expense")
    print("6. Search Expense")
    print("7. Delete Expense")
    print("8. Update Expense")
    print("9. Exit")
    print("10. Monthly Expense")
    print("11. Category-wise Summary")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense(expenses)
        save_expenses(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        calculate_total(expenses)

    elif choice == "4":
        find_highest(expenses)

    elif choice == "5":
        find_lowest(expenses)

    elif choice == "6":
        search_expense(expenses)

    elif choice == "7":
        delete_expense(expenses)
        save_expenses(expenses)

    elif choice == "8":
        update_expense(expenses)
        save_expenses(expenses)

    elif choice == "9":
        save_expenses(expenses)
        print("\nExpenses saved successfully!")
        print("Thank you for using Expense Tracker!")
        break

    elif choice == "10":
        monthly_expense(expenses)

    elif choice == "11":
        category_summary(expenses)

    else:
        print("\nInvalid choice. Please enter a number from 1 to 11.")