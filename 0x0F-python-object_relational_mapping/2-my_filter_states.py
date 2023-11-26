#!/usr/bin/python3
"""
2-my_filter_states.py - Displays all values in the 'states' table of the database hbtn_0e_0_usa
whose name matches that supplied as an argument.

Usage:
  ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>

Description:
  This script connects to a MySQL database and retrieves records from the 'states' table where
the state name matches the provided argument. It is designed to be executed from the command line
with four required arguments:
  - <mysql username>: The username to connect to the MySQL database.
  - <mysql password>: The password associated with the provided username.
  - <database name>: The name of the MySQL database containing the 'states' table.
  - <state name searched>: The state name to search for in the 'states' table.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database using command-line arguments
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    c = db.cursor()

    # Execute a MySQL query to select records from the 'states' table
    # where the state name matches the provided argument
    c.execute("SELECT * FROM `states` WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    # Print the retrieved states
    [print(state) for state in c.fetchall()]
