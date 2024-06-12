from lib.database import CONN, CURSOR

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

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM Transactions')
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, transaction_id):
        CURSOR.execute('SELECT * FROM Transactions WHERE transaction_id=?', (transaction_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    def update(self, amount, date, category_id, description):
        CURSOR.execute('''
            UPDATE Transactions
            SET amount=?, date=?, category_id=?, description=?
            WHERE transaction_id=?
        ''', (amount, date, category_id, description, self.transaction_id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM Transactions WHERE transaction_id=?', (self.transaction_id,))
        CONN.commit()
