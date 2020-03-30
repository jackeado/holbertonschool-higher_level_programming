#!/usr/bin/python3
"""
 lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
import MySQLdb
import SQLAlchemy
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        db=MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
