#!/usr/bin/python3
"""
13-model_state_delete_a.py - Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

Usage:
  ./13-model_state_delete_a.py <mysql username> <mysql password> <database name>

Description:
  This script connects to a MySQL database using SQLAlchemy and deletes all State objects
  from the 'states' table with a name containing the letter 'a'. It is designed to be executed
  from the command line with three required arguments:
  - <mysql username>: The username to connect to the MySQL database.
  - <mysql password>: The password associated with the provided username.
  - <database name>: The name of the MySQL database containing the 'states' table.

Requirements:
  - Python 3
  - SQLAlchemy library
  - model_state module (containing the State class)

Note:
  Ensure that the 'model_state' module is available and contains the State class definition.

Example:
  $ ./13-model_state_delete_a.py root password hbtn_0e_6_usa
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

    # Delete all State objects with a name containing the letter 'a'
    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()
