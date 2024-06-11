import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

def initalize_db():
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