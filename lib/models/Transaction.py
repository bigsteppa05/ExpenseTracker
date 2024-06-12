import sqlite3
from lib.models import CONN, CURSOR

class Transaction:
    def __init__(self, transaction_id, amount, date, category_id, description):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.category_id = category_id
        self.description = description

    @classmethod
    def create(cls, amount, date, category_id, description):
        CURSOR.execute('''
            INSERT INTO Transactions (amount, date, category_id, description)
            VALUES (?, ?, ?, ?)
        ''', (amount, date, category_id, description))
        CONN.commit()
        return cls(CURSOR.lastrowid, amount, date, category_id, description)

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM Transactions')
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, transaction_id):
        CURSOR.execute('SELECT * FROM Transactions WHERE transaction_id = ?', (transaction_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None

    def update(self, amount, date, category_id, description):
        CURSOR.execute('''
            UPDATE Transactions
            SET amount = ?, date = ?, category_id = ?, description = ?
            WHERE transaction_id = ?
        ''', (amount, date, category_id, description, self.transaction_id))
        CONN.commit()
        self.amount = amount
        self.date = date
        self.category_id = category_id
        self.description = description

    def delete(self):
        CURSOR.execute('DELETE FROM Transactions WHERE transaction_id = ?', (self.transaction_id,))
        CONN.commit()

    def __repr__(self):
        return f"Transaction(transaction_id={self.transaction_id}, amount={self.amount}, date='{self.date}', category_id={self.category_id}, description='{self.description}')"

