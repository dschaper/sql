"""Prompt the user whether he or she would like to perform an aggregation (AVG, MAX,
MIN, or SUM) or exit the program altogether."""

import sqlite3

agg = {"average": "SELECT AVG(num) FROM numbers",
       "maximum": "SELECT MAX(num) FROM numbers",
       "minimum": "SELECT MIN(num) FROM numbers",
       "sum": "SELECT sum(num) FROM numbers"}

inp = raw_input("Please choose an aggregate function: ")

selection = agg.get(inp, None)

if selection == None:
    print "Exiting"
    exit()

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    c.execute(selection)

    result = c.fetchone()[0]
    print "{}: {}".format(inp, result)