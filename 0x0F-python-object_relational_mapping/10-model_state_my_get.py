#!/usr/bin/python3
"""script that prints the State object with the name passed as argument
   from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    aux = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    # You can assume you have one record with the state name to search
    for state in session.query(State).order_by(State.id).\
            filter(State.name == argv[4]).all():
        print("{}".format(state.id))
        aux = 1
    if (aux == 0):
        print("Not Found")

    session.close()
