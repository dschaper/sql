import random
import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num INT)")

    for _ in xrange(100):
        num = random.randint(0, 100)
        c.execute("INSERT INTO numbers VALUES(?)", (num,))
