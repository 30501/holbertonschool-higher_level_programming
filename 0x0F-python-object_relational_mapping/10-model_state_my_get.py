#!/usr/bin/python3
"""script that prints the State object with the name passed as argument
   from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    # You can assume you have one record with the state name to search
    find_state = session.query(State).filter(State.name == argv[4]).first()
    session.close()

    if (find_state is None):
        print("Not Found")
    else:
        print("{}".format(find_state.id))

    # session.close()
