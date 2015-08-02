""" Add another table to accompany your "inventory" table called "orders". This table
    should have the following fields: "make", "model", and "order_date". Make sure to
    only inluce makes and models for the cars found in the inventory table. Add 15 records
    (3 for each car), each with a separate order date (YYYY-MM-DD)."""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE orders('make' TEXT, 'model' TEXT, 'order_date' DATE)")

    orders = [('Ford', 'Taurus', '2015-01-02'),
              ('Ford', 'Taurus', '2014-12-25'),
              ('Ford', 'Taurus', '2015-02-14'),
              ('Honda', 'Accord', '2015-01-04'),
              ('Honda', 'Accord', '2014-10-04'),
              ('Honda', 'Accord', '2015-06-11'),
              ('Ford', 'Fiesta', '2104-08-06'),
              ('Ford', 'Fiesta', '2015-06-12'),
              ('Ford', 'Fiesta', '2014-12-31'),
              ('Honda', 'Civic', '2015-02-23'),
              ('Honda', 'Civic', '2015-03-12'),
              ('Honda', 'Civic', '2015-07-11'),
              ('Ford', 'F-150', '2013-12-31'),
              ('Ford', 'F-150', '2015-12-01'),
              ('Ford', 'F-150', '2014-08-28')]

    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)
