#!/usr/bin/python3
"""
relationship_state.py - Defines a State model.
Inherits from SQLAlchemy Base and links to the MySQL table 'states'.

Attributes:
    id (int): The state's id.
    name (str): The state's name.
    cities (sqlalchemy.orm.relationship): The State-City relationship.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

Base = declarative_base()

class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        id (int): The state's id.
        name (str): The state's name.
        cities (sqlalchemy.orm.relationship): The State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
