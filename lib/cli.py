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