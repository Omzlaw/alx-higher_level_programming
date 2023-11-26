#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py - Lists all City objects from the database hbtn_0e_14_usa.

Usage:
  ./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>

Description:
  This script connects to a MySQL database using SQLAlchemy and retrieves all City objects
  along with their corresponding State names from the 'cities' and 'states' tables. The results
  are ordered by City id. It is designed to be executed from the command line with three required arguments:
  - <mysql username>: The username to connect to the MySQL database.
  - <mysql password>: The password associated with the provided username.
  - <database name>: The name of the MySQL database containing the 'cities' and 'states' tables.

Requirements:
  - Python 3
  - SQLAlchemy library
  - model_state module (containing the State class)
  - model_city module (containing the City class)

Note:
  Ensure that the 'model_state' and 'model_city' modules are available and contain the State and City class definitions.

Example:
  $ ./14-model_city_fetch_by_state.py root password hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    # Create a connection to the MySQL database using SQLAlchemy
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and print all City objects along with their corresponding State names
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
