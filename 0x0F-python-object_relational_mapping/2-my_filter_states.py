#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the
states table of the database hbtn_0e_0_usa where name matches
the argument.
"""

import sys
import MySQLdb


def list_states_with_name(
        mysql_username, mysql_password, database_name, state_name):
    """
    Connect to the MySQL database and list all states
    with the specified name.

    Args:
        state_name (str): The name of the state to search for.

    Returns:
        None
    """
    # Connect to the MySQL database
    db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=mysql_username,
                password=mysql_password,
                db=database_name
            )

    cursor = db.cursor()

    # Define the SQL query with user input
    query = (
            "SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC"
            .format(state_name)
            )
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Main function to get command line arguments and call
    the class method to list states.
    """
    # Get the MySQL credentials and database name and
    # state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to list states with the specified name
    list_states_with_name(
            mysql_username, mysql_password, database_name, state_name)
