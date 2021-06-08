import os
import csv
from importlib import resources
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Athlete_Info, Athlete, Federation, Lift, Location, Meet


def get_lifting_data(filepath):
    with open(filepath) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]
        return data


def populate_database(session, lifting_data):

    for i, row in enumerate(lifting_data):
        if i % 1000 == 0:
            print(i)
        athlete = (
            session.query(Athlete)
            .filter(Athlete.name == row['Name'])
            .one_or_none()
        )

        if athlete is None:
            athlete = Athlete(
                name=row["Name"]
            )
            session.add(athlete)

        federation = (
            session.query(Federation)
            .filter(Federation.name == row['Federation'])
            .one_or_none()
        )

        if federation is None:
            federation = Federation(
                name=row["Federation"]
            )
            session.add(federation)

        lift = Lift(
            squat_1_kg = row["Squat1Kg"] if row["Squat1Kg"] else None,
            squat_2_kg = row["Squat2Kg"] if row["Squat2Kg"] else None,
            squat_3_kg = row["Squat3Kg"] if row["Squat3Kg"] else None,
            squat_4_kg = row["Squat4Kg"] if row["Squat4Kg"] else None,
            best_3_squat_kg = row["Best3SquatKg"] if row["Best3SquatKg"] else None,
            bench_1_kg = row["Bench1Kg"] if row["Bench1Kg"] else None,
            bench_2_kg = row["Bench2Kg"] if row["Bench2Kg"] else None,
            bench_3_kg = row["Bench3Kg"] if row["Bench3Kg"] else None,
            bench_4_kg = row["Bench4Kg"] if row["Bench4Kg"] else None,
            best_3_bench_kg = row["Best3BenchKg"] if row["Best3BenchKg"] else None,
            deadlift_1_kg = row["Deadlift1Kg"] if row["Deadlift1Kg"] else None,
            deadlift_2_kg = row["Deadlift2Kg"] if row["Deadlift2Kg"] else None,
            deadlift_3_kg = row["Deadlift3Kg"] if row["Deadlift3Kg"] else None,
            deadlift_4_kg = row["Deadlift4Kg"] if row["Deadlift4Kg"] else None,
            best_3_deadlift_kg = row["Best3DeadliftKg"] if row["Best3DeadliftKg"] else None,
        )
        session.add(lift)

        athlete.lifts.append(lift)
        # author.publishers.append(publisher)
        # publisher.authors.append(author)
        # publisher.books.append(book)
        session.commit()

    session.close()


def main():
    print("starting")

    data = get_lifting_data('lifting.csv')

    lifting_data = data

    if os.path.exists('lifting.db'):
        os.remove('lifting.db')

    # create the database
    engine = create_engine(f"sqlite:///lifting.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    populate_database(session, lifting_data)

    print("finished")


if __name__ == "__main__":
    main()
