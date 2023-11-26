#!/usr/bin/python3
"""
0-select_states.py - Lists all states from the database hbtn_0e_0_usa.

Usage:
  ./0-select_states.py <mysql username> <mysql password> <database name>

Description:
  This script connects to a MySQL database and retrieves all records from the 'states' table.
  It is designed to be executed from the command line with three required arguments:
  - <mysql username>: The username to connect to the MySQL database.
  - <mysql password>: The password associated with the provided username.
  - <database name>: The name of the MySQL database containing the 'states' table.

Requirements:
  - Python 3
  - MySQLdb module

Example:
  $ ./0-select_states.py root password hbtn_0e_0_usa

Note:
  Make sure to replace 'root', 'password', and 'hbtn_0e_0_usa' with your MySQL username,
  password, and the name of the database, respectively.

Author:
  [Your Name]
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

    # Execute a MySQL query to select all records from the 'states' table
    c.execute("SELECT * FROM `states`")

    # Print the retrieved states
    [print(state) for state in c.fetchall()]

