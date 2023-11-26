#!/usr/bin/python3
"""
12-model_state_update_id_2.py - Changes the name of the State object with id = 2 to "New Mexico"
in the database hbtn_0e_6_usa.

Usage:
  ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>

Description:
  This script connects to a MySQL database using SQLAlchemy and updates the name of the State object
  with id = 2 to "New Mexico" in the 'states' table. It is designed to be executed from the command line
  with three required arguments:
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
  $ ./12-model_state_update_id_2.py root password hbtn_0e_6_usa
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

    # Retrieve the State object with id = 2 and update its name to "New Mexico"
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
