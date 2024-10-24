import sqlite3
from sqlite3 import Error

db_account = './db/databases/users.db'
db_passwords = './db/databases/passwords.db'

def acess_db(db_name):
    try:
        conn=sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)
    return None


def auth_user(email, password):
    conn = acess_db(db_account)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def get_user(email):
    conn = acess_db(db_account)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def reg_user(email, password):
    conn = acess_db(db_account)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    conn.close()
    
def create_password(email, password, source):
    conn = acess_db(db_passwords)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (email, account, password) VALUES (?, ?, ?)", (email, password, source))
    conn.commit()
    conn.close()
    
def get_passwords(email):
    conn = acess_db(db_passwords)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords WHERE email = ?", (email,))
    senhas = cursor.fetchall()
    conn.close()
    return senhas

def delete_passwords(id):
    conn = acess_db(db_passwords)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE id = ?", (id,))
    conn.commit()
    conn.close()