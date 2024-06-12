from lib.database import CONN, CURSOR

class Budget:
    def __init__(self, budget_id=None, category_id=None, budget_limit=None):
        self.budget_id = budget_id
        self.category_id = category_id
        self.budget_limit = budget_limit

        @classmethod
        def create_table(cls):
            CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS Budgets(
                budget_id INTEGER PRIMARY KEY,
                category_id INTEGER,
                budget_limit REAL NOT NULL,
                FOREIGN KEY (category_id) REFERENCES Categories(category_id)
            )
            ''')
            CONN.commit


        @classmethod
        def create(cls, category_id, budget_limit):
            CURSOR.execute('''
            INSERT INTO budgets (category_id, budget_limit
            VALUES (?, ?)
            ''', (category_id, budget_limit))
            CONN.commit()
            return cls(CURSOR.lastrowid, category_id, budget_limit)

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM Budgets')
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, budget_id):
        CURSOR.execute('SELECT * FROM Budgets WHERE budget_id = ?', (budget_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    def update(self, category_id, budget_limit):
        CURSOR.execute('''
        UPDATE Budgets SET category_id = ?, budget_limit = ?
        WHERE budget_id = ?
        ''', (category_id, budget_limit, self.budget_id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM Budgets WHERE budget_id = ?', (self.budget_id,))
        CONN.commit()