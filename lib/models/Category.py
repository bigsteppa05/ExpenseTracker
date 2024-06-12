from lib.database import CONN, CURSOR

class Category:
    def __init__(self, category_id=None, name=None):
        self.category_id = category_id
        self.name = name

    @classmethod
    def create(cls, name):
        CURSOR.execute('''
        INSERT INTO Categorie (name)  VALUES (?)
        ''', (name,))  
        CONN.commit()  
        return cls(CURSOR.lastrowid, name)
    
    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM Categories')
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]
    
    @classmethod
    def find_by_id(cls, category_id):
        CURSOR.execute('SELECT * FROM Categories WHERE category_id = ?', (category_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None
    
    def update(self, name):
        CURSOR.execute('''
        UPDATE Categories SET name = ? WHERE category_id = ?
        ''', (name, self.category_id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM Categories WHERE category_id = ?', (self.category_id,))
        CONN.commit()
    

        