#!/usr/bin/python3
"""
100-relationship_states_cities.py - Creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa.

Usage:
  ./100-relationship_states_cities.py <mysql username> <mysql password> <database name>

Description:
  This script connects to a MySQL database using SQLAlchemy and creates the State "California"
  with the City "San Francisco" using the relationship defined in the 'relationship_state' and
  'relationship_city' modules. It is designed to be executed from the command line with three
  required arguments:
  - <mysql username>: The username to connect to the MySQL database.
  - <mysql password>: The password associated with the provided username.
  - <database name>: The name of the MySQL database containing the 'states' and 'cities' tables.

Requirements:
  - Python 3
  - SQLAlchemy library
  - relationship_state module (containing the State class)
  - relationship_city module (containing the Base and City classes)

Note:
  Ensure that the 'relationship_state' and 'relationship_city' modules are available and contain
  the State, Base, and City class definitions.

Example:
  $ ./100-relationship_states_cities.py root password hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create a connection to the MySQL database using SQLAlchemy
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create the tables defined in the Base class
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new City "San Francisco" associated with the State "California"
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
