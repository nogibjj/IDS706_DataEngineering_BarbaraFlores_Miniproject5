"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="data/WorldSmall.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())

    with open(dataset, 'r', encoding='utf-8', newline='') as file:
        payload = csv.reader(file, delimiter=',')

        conn = sqlite3.connect('WorldSmallDB.db')
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS WorldSmallDB")
        c.execute("CREATE TABLE WorldSmallDB (country, region, gdppcap08, polityIV)")
        #insert
        c.executemany("INSERT INTO WorldSmallDB VALUES (?, ?, ?, ?)", payload)
        conn.commit()
        conn.close()
    return "WorldSmallDB.db"