#!/usr/bin/python3
"""
10-model_state_my_get.py - Lists the State object with the name passed as an argument
from the database hbtn_0e_6_usa.

Usage:
  ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name searched>

Description:
  This script connects to a MySQL database using SQLAlchemy and retrieves the State object
  from the 'states' table that matches the provided state name. It is designed to be executed
  from the command line with four required arguments:
  - <mysql username>: The username to connect to the MySQL database.
  - <mysql password>: The password associated with the provided username.
  - <database name>: The name of the MySQL database containing the 'states' table.
  - <state name searched>: The state name to search for in the 'states' table.

Requirements:
  - Python 3
  - SQLAlchemy library
  - model_state module (containing the State class)

Note:
  Ensure that the 'model_state' module is available and contains the State class definition.

Example:
  $ ./10-model_state_my_get.py root password hbtn_0e_6_usa California
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a connection to the MySQL database using SQLAlchemy
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for the State object with the provided name and print its ID
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if not found:
        print("Not found")
