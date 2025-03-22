import tkinter as tk
from . database import database_object, Cursor

# Queries
create_table_query = """CREATE TABLE users IF NOT EXITS (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)"""
insert_new_user_query = """INSERT INTO users (username, password) VALUES (?,?)""".format(username, password)


database_object = Database(database_name='ChatDatabase.db')
query_insert = """INSERT INTO users"""


def validate_user(username:str, password:str, cursor:Cursor) -> bool:
    """
        Validate user's provided data to check if user exists or not.
    """
    cursor = cursor
    
    # Behavior
    cursor.execute_select_query()
    
    user = None
    return user not None
   
   
   
root = tk.Tk()
root.title("Chat With Sockets | MarcoA-Pozol")
root.size("1200x600+0+0")

register_formulary = tk.Label(root, bg='blue', fg='white')
register_formulary.position(x=50, y=50)

# username field
username_label = tk.Label(register_formulary, fg='white')
username_label.grid(row=0, column=0)

username_entry = tk.Entry(register_formulary, fg='white', bg='green')
username_entry.grid(row=0, column=1)


# password field
password_label = tk.Label(register_formulary, fg='white')
password_label.grid(row=1, column=0)

password_entry = tk.Entry(register_formulary, fg='white', bg='green')
password_entry.grid(row=1, column=1)

button_register = tk.Button(register_formulary, text="Create", command=lambda:validate_user(username=username_entry.get(), password=password_entry.get()))
root.mainloop()