""" Update the quantity on two of the records, and then output all 
    of the records from the table."""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE inventory SET Quantity = 5 WHERE Model='Taurus'")
    c.execute("UPDATE inventory SET Quantity = 1 WHERE Model='Accord'")

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]