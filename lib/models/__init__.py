import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

def initialize_db():
    CURSOR.execute('''
    CREATE TABLE IF  NOR EXISTS Transactions (
        transaction_id INTEGER PRIMARY KEY,
        amount REAL NOT NULL,
        date TEXT NOT NULL,
        category_id INTEGER,
        description TEXT,
        FOREIGN KEY (category_id) REFERENCES Categories(category_id)                    
    )             
        ''' )
    
    CURSOR.execute('''
    CREATE TABLE IF NOT EXISTS Budget (
        budget_id INTEGER PRIMARY KEY,
        category_id INTEGER,
        LIMIT REAL NOT NULL,
        FOREIGN KEY (category_id) REFERENCES Categories(category_id)
    )       
        ''')
    
    CUROR.execute('''
    CREATE TABLE IF NOT EXISTS Categories(
        category_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    )       
        ''')
 
    CONN.commit()


if __name__== '__main__':
    initialize_db()
    print("Database initialized")