#!/usr/bin/python3
"""
102-relationship_cities_states_list.py - Lists all City objects from the database hbtn_0e_101_usa.

Usage:
  ./102-relationship_cities_states_list.py <mysql username> <mysql password> <database name>

Description:
  This script connects to a MySQL database using SQLAlchemy and retrieves all City objects from
  the 'cities' table along with their corresponding State names using the relationship defined in
  the 'relationship_state' and 'relationship_city' modules. It is designed to be executed from the
  command line with three required arguments:
  - <mysql username>: The username to connect to the MySQL database.
  - <mysql password>: The password associated with the provided username.
  - <database name>: The name of the MySQL database containing the 'cities' and 'states' tables.

Requirements:
  - Python 3
  - SQLAlchemy library
  - relationship_state module (containing the State class)
  - relationship_city module (containing the City class)

Note:
  Ensure that the 'relationship_state' and 'relationship_city' modules are available and contain
  the State, Base, and City class definitions.

Example:
  $ ./102-relationship_cities_states_list.py root password hbtn_0e_101_usa
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

    # Retrieve and print all City objects along with their corresponding State names
    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
