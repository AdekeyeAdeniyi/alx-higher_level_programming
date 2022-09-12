#!/usr/bin/python3
"""
This script delet state objects
which conatains letter `a`
in database hbtn_0e_6_usa
"""
from sys import argv
from unicodedata import name
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    rows = session.query(State).filter(State.name.contains('a'))
    
    for data in rows:
        session.delete(data)
    session.commit()
    session.close()
