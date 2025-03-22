import tkinter as tk
from . database import database_object

# Queries
create_table_query = """CREATE TABLE users IF NOT EXITS (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)"""
insert_new_user_query = """INSERT INTO users (username, password) VALUES (?,?)""".format(username, password)

database_object.execute_query(query=create_table_query)
query_insert = """INSERT INTO users"""


def validate_user(username:str, password:str) -> bool:
    """
        Validate user's provided data to check if user exists or not.
    """
    
    user = None
    return user not None