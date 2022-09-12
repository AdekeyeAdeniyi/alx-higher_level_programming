#!/usr/bin/python3
"""
    Python file that contains the class definition of a State 
    and an instance Base for MySQLAlchemy ORM
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, Integer, String

#MANAGE TABLES
Base = declarative_base()

class State(Base):
    """An ORM class for state database

    Attributes
    ----------
    __tablename__: str
        Name of table
    id: integr
        The state index number
    name : str
        The name of the state
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key = True)
    name = Column(String(128), nullable = False)

    def __init__(self, id, name):
        """
        Parameters
        ----------
        id: integr
            The state index number
        name : str
            The name of the state
        """
        self.id = id,
        self.name = name
