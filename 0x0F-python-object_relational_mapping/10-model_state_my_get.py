#!/usr/bin/python3
"""
This script print state objects
with name passed as argument
from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    data = session.query(State).where(State.name == argv[4]).first()

    if data is None:
        print('Not found')
    else:
        print('{0}'.format(data.id))
