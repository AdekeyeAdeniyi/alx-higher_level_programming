#!/usr/bin/python3
"""
This script delet state objects
which conatains letter `a`
in database hbtn_0e_6_usa
"""
from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    queries = session.query(State).outerjoin(
        City).order_by(State.id, City.id).all()

    for _state in queries:
        print(f'{_state.id}: {_state.name}')

        for _city in _state.cities:
            print(f'    {_city.id}: {_city.name}')
