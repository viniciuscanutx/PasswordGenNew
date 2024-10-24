import flet as ft 
import sqlite3
from sqlite3 import Error
import random 
import string

db_account = './db/users.db'
db_passwords = './db/passwords.db'

def acess_db(db_name):
    try:
        conn=sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)
    return None