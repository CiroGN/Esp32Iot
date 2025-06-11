import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.conn = sqlite3.connect('ecommerce.db')
        self.cursor = self.conn.cursor()
        pass

    def createTables(self):
        # Cliente
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS registro_token (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT NOT NULL
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS registro_presence (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timeStamp REAL
            registro_token INTEGER NOT NULL,
            FOREIGN KEY (registro_token) REFERENCES registro_token(id)
        )
        ''')

        self.conn.commit()

    def close(self):
        self.conn.close()

    def query(self, command):
        self.cursor.execute(command)

    def select(self, query):
        self.cursor.execute(query)
        resultado = self.cursor.fetchall()
        return resultado