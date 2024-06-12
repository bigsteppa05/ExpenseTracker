from lib.models.Category import Category
from lib.models.Budget import Budget
from lib.models.Transaction import Transaction

def main_menu():
    while True:
        print("Main Menu")
        print("1. Manage Categories")
        print("2. Manage Transactions")
        print("3. Manage Budgets")
        print("4. Exit")
        choice = input("Choose an option")

        if choice == '1':
            manage_categories()
        elif choice == '2':
            manage_transactions()
        elif choice =="3":
            manage_budgets()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

    
def manage_categories():
    while True:
        print("Categories Menu")
        print("1. Create Category")
        print("2. View All Categories")
        print("3. Update Category")
        print("4. Delete Category")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter category name: ")
            Category.create(name)
            print("Category created successfully.")
        elif choice == '2':
            categories = Category.get_all()
            for category in categories:
                print(f"{category.category_id}: {category.name}")
        elif choice == '3':
            category_id = int(input("Enter category ID to update: "))
            name = input("Enter new category name: ")
            category = Category.find_by_id(category_id)
            if category:
                category.update(name)
                print("Category updated successfully.")
            else:
                print("Category not found.")
        elif choice == '4':
            category_id = int(input("Enter category ID to delete: "))
            category = Category.find_by_id(category_id)
            if category:
                category.delete()
                print("Category deleted successfully.")
            else:
                print("Category not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")


def manage_transactions():
    while True:
        print("Transactions Menu")
        print("1. Create Transaction")
        print("2. View All Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction ")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            category_id = int(input("Enter category ID: "))
            description = input("Enter description: ")
            Transaction.create(amount, date, category_id, description)
            print("Transaction created successfully.")
        elif choice == '2':
            transactions = Transaction.get_all()
            for transaction in transactions:
                print(f"{transaction.transaction_id}: {transaction.amount}, {transaction.date}, {transaction.category_id}, {transaction.description}")
        elif choice == '3':
            transaction_id = int(input("Enter transaction ID to update: "))
            transaction = Transaction.find_by_id(transaction_id)
            if transaction:
                amount = float(input("Enter new amount: "))
                date = input("Enter new date (YYYY-MM-DD): ")
                category_id = int(input("Enter new category ID: "))
                description = input("Enter new description: ")
                transaction.update(amount, date, category_id, description)
                print("Transaction updated successfully.")
            else:
                print("Transaction not found.")
        elif choice == '4':
            transaction_id = int(input("Enter transaction ID to delete: "))
            transaction = Transaction.find_by_id(transaction_id)
            if transaction:
                transaction.delete()
                print("Transaction deleted successfully.")
            else:
                print("Transaction not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")



def manage_budgets():
    while True:
        print("Budgets Menu")
        print("1. Create Budget")
        print("2. View All Budgets")
        print("3. Update Budget")
        print("4. Delete Budget")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            category_id = int(input("Enter category ID: "))
            budget_limit = float(input("Enter budget limit: "))
            Budget.create(category_id, budget_limit)
            print("Budget created successfully.")
        elif choice == '2':
            budgets = Budget.get_all()
            for budget in budgets:
                print(budget)
        elif choice == '3':
            budget_id = int(input("Enter budget ID to update: "))
            budget = Budget.find_by_id(budget_id)
            if budget:
                category_id = int(input("Enter new category ID: "))
                budget_limit = float(input("Enter new budget limit: "))
                budget.update(category_id, budget_limit)
                print("Budget updated successfully.")
            else:
                print("Budget not found.")
        elif choice == '4':
            budget_id = int(input("Enter budget ID to delete: "))
            budget = Budget.find_by_id(budget_id)
            if budget:
                budget.delete()
                print("Budget deleted successfully.")
            else:
                print("Budget not found.")
        elif choice == '5':
            return
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()