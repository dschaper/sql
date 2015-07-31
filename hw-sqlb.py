""" Using the 'inventory' table from the previous homework assignment,
    add (INSERT) 5 records (rows of data) to the table. Make sure 3
    of the vehicles are Fords while the other 2 are Hondas.
    Use any model and quantity for each
"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [("Ford", "Taurus", 2),
            ("Honda", "Accord", 3),
            ("Ford", "Fiesta", 1),
            ("Honda", "Civic", 3),
            ("Ford", "F-150", 4)
        ]

    # INSERT data into table
    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars)
