#!/usr/bin/python3
"""
5-filter_cities.py - Displays all cities of a given state from the 'states' table of the database hbtn_0e_4_usa.
Safe from SQL injections.

Usage:
  ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name searched>

Description:
  This script connects to a MySQL database and retrieves all cities from the 'cities' table,
  along with their corresponding state names from the 'states' table. The results are ordered
  by city id. The script is designed to be executed from the command line with four required arguments:
  - <mysql username>: The username to connect to the MySQL database.
  - <mysql password>: The password associated with the provided username.
  - <database name>: The name of the MySQL database containing the 'cities' and 'states' tables.
  - <state name searched>: The state name to filter cities by.

Note:
  This script is designed to be safe from SQL injections by using parameters in the query.

Requirements:
  - Python 3
  - MySQLdb module
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

    # Execute a MySQL query to select city information along with state names
    # from the 'cities' and 'states' tables, ordered by city id
    c.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

    # Print the retrieved cities of the given state
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
