import sqlite3

conn = sqlite3.connect('./db/users.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    );
''')

conn.commit()
conn.close()

conn = sqlite3.connect('./db/passwords.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    account TEXT NOT NULL,
    password TEXT NOT NULL
    );
''')

conn.commit()
conn.close()

print("Ok.")