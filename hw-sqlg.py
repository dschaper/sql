"""Using the COUNT() function, calculate the total number of orders for each make and
model"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()
    for r in rows:
        print r[0], r[1]
        print r[2]
        c.execute("SELECT count(order_date) FROM orders WHERE model=?", (r[1],))
        print c.fetchone()[0]