#!/usr/bin/python3
"""
101-relationship_states_cities_list.py - Lists all States and corresponding Cities in the database hbtn_0e_101_usa.

Usage:
  ./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>

Description:
  This script connects to a MySQL database using SQLAlchemy and retrieves all States and their corresponding
  Cities from the 'states' and 'cities' tables using the relationship defined in the 'relationship_state' and
  'relationship_city' modules. It is designed to be executed from the command line with three required arguments:
  - <mysql username>: The username to connect to the MySQL database.
  - <mysql password>: The password associated with the provided username.
  - <database name>: The name of the MySQL database containing the 'states' and 'cities' tables.

Requirements:
  - Python 3
  - SQLAlchemy library
  - relationship_state module (containing the State class)
  - relationship_city module (containing the City class)

Note:
  Ensure that the 'relationship_state' and 'relationship_city' modules are available and contain
  the State, Base, and City class definitions.

Example:
  $ ./101-relationship_states_cities_list.py root password hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create a connection to the MySQL database using SQLAlchemy
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and print all States and their corresponding Cities
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
