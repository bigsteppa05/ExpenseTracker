# Expense Tracker CLI Application

## Overview

The Expense Tracker CLI application is designed to help users efficiently track their expenses and income. The application allows users to add, categorize, and manage transactions, set budgets for different categories, and generate financial reports.

## Problem Statements

1. **Manual Tracking Challenges**: Users often struggle with manually tracking their expenses and income, leading to errors and inefficiencies.
2. **Lack of Organization**: Without proper categorization, analyzing spending patterns and budgeting effectively becomes difficult.
3. **Inadequate Financial Insights**: Users need a simple way to generate reports that provide insights into their financial health.

## Solution

To address the identified problems, the Expense Tracker CLI application provides the following solutions:

- **Automated Tracking**: The application allows users to easily add and manage their transactions, reducing manual tracking errors and inefficiencies.
- **Categorization**: Users can categorize transactions into predefined categories, making it easier to organize and analyze spending patterns.
- **Financial Insights**: The application can generate detailed financial reports, providing users with insights into their financial health and helping them make informed budgeting decisions.

## Database Schema

The application uses a SQLite database with the following tables:

1. **Transactions**
   - `transaction_id` (INTEGER, Primary Key): Uniquely identifies each transaction.
   - `amount` (REAL): Amount of the transaction.
   - `date` (TEXT): Date of the transaction.
   - `category_id` (INTEGER, Foreign Key): Links to the Categories table.
   - `description` (TEXT): Description of the transaction.

2. **Categories**
   - `category_id` (INTEGER, Primary Key): Uniquely identifies each category.
   - `name` (TEXT): Name of the category.

3. **Budgets**
   - `budget_id` (INTEGER, Primary Key): Uniquely identifies each budget entry.
   - `category_id` (INTEGER, Foreign Key): Links to the Categories table.
   - `limit` (REAL): Budget limit for the category.

## Relationships

### Transactions and Categories

- **One-to-Many Relationship**: Each transaction belongs to one category, but a single category can include many transactions.
- **Foreign Key Constraint**: The `category_id` in the Transactions table links each transaction to a specific category in the Categories table.

### Budgets and Categories

- **One-to-One Relationship**: Each budget entry is associated with one category, and each category can have only one budget entry.
- **Foreign Key Constraint**: The `category_id` in the Budgets table links each budget entry to a specific category in the Categories table.

## Project MVP Features

### Transaction Management

- Users can add, view, edit, and delete transactions (expenses and income).
- Transactions include an amount, date, category, and description.

### Categorization

- Users can categorize transactions into predefined categories.

### Budget Management

- Users can set and manage budget limits for different categories.

### Reporting

- Generate reports to provide insights into users' financial health.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ExpenseTracker.git
   cd ExpenseTracker

 2. Create and activate a virtual environment:

 python3 -m venv venv
 source venv/bin/activate

  3. Install dependencies:

 pip install pipenv
 pipenv install

  4. Initialize the database:

  python3 lib/models/__init__.py
  Usage
 
  5. Run the CLI application:
  
  python3 cli.py


##  Main Menu
Manage Categories
Manage Transactions
Manage Budgets
Exit
##  Manage Categories
Create Category
View All Categories
Update Category
Delete Category
Back to Main Menu
##  Manage Transactions
Create Transaction
View All Transactions
Update Transaction
Delete Transaction
Back to Main Menu
##  Manage Budgets
Create Budget
View All Budgets
Update Budget
Delete Budget
Back to Main Menu
##  Example
1. Creating a Category:

Choose an option: 1
Enter category name: Food
Category created successfully.

2. Creating a Transaction:

Choose an option: 1
Enter amount: 50
Enter date (YYYY-MM-DD): 2023-06-15
Enter category ID: 1
Enter description: Groceries
Transaction created successfully.

3. Viewing All Transactions:

Choose an option: 2
Transaction(transaction_id=1, amount=50.0, date='2023-06-15', category_id=1, description='Groceries')
##  Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License.

Acknowledgements

## Contacts

For any inquiries, issues, or suggestions related to the Expense Tracker CLI application, please feel free to contact:

Name: [Habib Mohamed]
Email: [habibforderiv05@gmail.com]
GitHub:@bigsteppa05
Feel free to reach out with any questions or feedback!





