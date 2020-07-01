import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row

def create_table():
    # We need context manager when making changes to the DB
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries(content TEXT, date TEXT);"
        )

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES(?, ?);", (entry_content, entry_date)
        )

def get_entries():
    # We don't need context manager here since we are not making any changes to the DB
    cursor =  connection.cursor()
    cursor.execute(
        "SELECT * FROM entries;"
    )
    return cursor