#!/usr/bin/python3

"""
    A script that lists all states from the database hbtn_0e_0_usa
    With capital `N`
"""


from sys import argv
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    sql =   "SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC"

    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
