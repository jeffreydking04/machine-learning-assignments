from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Athlete
from models import Lift

def main():

    engine = create_engine(f"sqlite:///lifting.db")
    # Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    lift = session.query(Lift).filter(Lift.lift_id == 3).one_or_none()
    print(f"Athlete's name: {lift.athlete.name}")

    session.close()


if __name__ == "__main__":
    main()