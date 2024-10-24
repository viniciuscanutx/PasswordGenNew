import sqlite3

def create_users_table():
    conn = sqlite3.connect('./db/users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    
    conn.commit()
    conn.close()

def create_passwords_table():
    conn = sqlite3.connect('./db/passwords.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            account TEXT NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    
    conn.commit()
    conn.close()

# Função para inicializar os bancos de dados (opcional)
def initialize_databases():
    create_users_table()
    create_passwords_table()

if __name__ == '__main__':
    initialize_databases()
    print("Tabelas criadas com sucesso.")
