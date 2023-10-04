"""Query the database"""

import sqlite3
from prettytable import PrettyTable

def query():
    conn = sqlite3.connect("/workspaces/IDS706_DataEngineering_BarbaraFlores_Miniproject5/data/WorldSmallDB.db")
    cursor = conn.cursor()

    print("\nLet's quickly review our database. Let's take a sample of how it is constructed.\n")
    cursor.execute("SELECT * FROM WorldSmallDB ORDER BY RANDOM() LIMIT 5")
    print_table(cursor, cursor.fetchall())

    print("\nHow many records per continent does our database have?\n")
    cursor.execute(
        "SELECT region, COUNT(*) FROM WorldSmallDB GROUP BY region"
    )
    print_table(cursor, cursor.fetchall())

    conn.close()

def print_table(cursor, data):
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]
    for row in data:
        table.add_row(row)
    print(table)

