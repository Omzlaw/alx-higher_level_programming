#!/usr/bin/python3
"""
4-cities_by_state.py - Lists all cities of the database hbtn_0e_4_usa, ordered by city id.

Usage:
  ./4-cities_by_state.py <mysql username> <mysql password> <database name>

Description:
  This script connects to a MySQL database and retrieves all cities from the 'cities' table,
  along with their corresponding state names from the 'states' table. The results are ordered
  by city id. It is designed to be executed from the command line with three required arguments:
  - <mysql username>: The username to connect to the MySQL database.
  - <mysql password>: The password associated with the provided username.
  - <database name>: The name of the MySQL database containing the 'cities' and 'states' tables.

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
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

    # Print the retrieved cities
    [print(city) for city in c.fetchall()]
