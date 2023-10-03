"""Query the database"""

import sqlite3


def query():
    conn = sqlite3.connect("/workspaces/IDS706_DataEngineering_BarbaraFlores_Miniproject5/WorldSmallDB.db")

    # Resto de tu código...
    # Por ejemplo, puedes agregar un cursor y ejecutar una consulta aquí
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM WorldSmallDB")
    print(cursor.fetchall())



query()