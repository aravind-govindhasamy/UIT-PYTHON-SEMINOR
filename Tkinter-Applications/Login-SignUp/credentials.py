import os
import base64
import sqlite3

if not os.path.exists('files/'):
    os.mkdir('files/')

class Database:
    def __init__(self):
        if not os.path.exists('files/credentials.db'):
            self.conn = sqlite3.connect('files/credentials.db')
            self.conn.execute('''CREATE TABLE credentials (
                    username text NOT NULL,
                    email text NOT NULL,
                    password text NOT NULL)
            ''')
            print('Database created successfully')
        else:
            self.conn = sqlite3.connect('files/credentials.db')

        self.cursor = self.conn.cursor()

    def show_table(self):
        self.cursor.execute('''SELECT name FROM sqlite_master WHERE type="table"''')
        print(self.cursor.fetchall())

    def insert_credential(self, values):
        query = "INSERT INTO credentials VALUES (?,?,?)"
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            return 'success'
        except Exception as e:
            print(e)
            return 'error'

    def fetch_credential(self, email):
        query = "SELECT * FROM credentials WHERE email=?"
        try:
            self.cursor.execute(query, (email,))
            data = self.cursor.fetchone()
            return data
        except Exception as e:
            print(e)
            return 'error'

    def fetch_all_creds(self):
        query = "SELECT * FROM credentials"
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(e)
            return 'error'

def encode_password(password):
    return base64.b64encode(password.encode('utf-8'))

def decode_password(password):
    return base64.b64decode(password).decode("utf-8")

# Example usage:
# db = Database()
# db.show_table()
# db.insert_credential(('user1', 'user1@email.com', encode_password('password123')))
# credentials = db.fetch_credential('user1@email.com')
# print(decode_password(credentials[2]))
# all_creds = db.fetch_all_creds()
# print(all_creds)
