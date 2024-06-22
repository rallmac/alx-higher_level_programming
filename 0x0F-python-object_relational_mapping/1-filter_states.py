#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


def list_states_starting_with_n(mysql_username, mysql_password, database_name):

    db = MySQLdb.connect(


                host="localhost",
                port=3306,
                user=mysql_username,
                password=mysql_password,
                db=database_name
            )

    cursor = db.cursor()
    query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    list_states_starting_with_n(mysql_username, mysql_password, database_name)
