from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from models import Athlete, Lift, Federation, Meet, Location

def main():

    engine = create_engine(f"sqlite:///lifting.db")
    # Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    lift = session.query(Lift).filter(Lift.lift_id == 3).one_or_none()
    print(f"Athlete's name: {lift.athlete.name}")

    # federation_meet_count = session.query(Federation, func.count('*').label("count")).join(Meet).group_by(Federation).all()
    # print(f"Federations meets count: {federation_meet_count[0][1]}")

    # location_meet_count = session.query(Location, func.count('*').label("count")).join(Meet).group_by(Location).all()
    # print(f"Locations meets count: {location_meet_count[2][0].meets}")

    # meets = session.query(Meet)
    # print(meets.count())

    # athletes = session.query(Athlete, func.count('*').label('count')).join(Lift).group_by(Athlete).one()
    # print(athletes)

    session.close()


if __name__ == "__main__":
    main()