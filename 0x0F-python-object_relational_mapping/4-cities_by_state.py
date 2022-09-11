#!/usr/bin/python3
"""
This script that displays all values 
in the cities from the database 
`hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("""SELECT 
                c.id, c.name, s.name
                FROM cities AS c
                JOIN state AS s
                ON c.state_id == s.id 
                ORDER BY c.id ASC
                """)

    rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
