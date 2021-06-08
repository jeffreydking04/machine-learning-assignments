"""
This program builds the author_book_publisher Sqlite database from the
author_book_publisher.csv file.
"""

import os
import csv
from importlib import resources
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Athlete_Info, Athlete, Federation, Lift, Location, Meet


def get_lifting_data(filepath):
    """
    This function gets the data from the csv file
    """
    with open(filepath) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]
        return data


def populate_database(session, lifting_data):
    # insert the data
    lifts = ['Squat1Kg','Squat2Kg','Squat3Kg','Squat4Kg','Best3SquatKg','Bench1Kg','Bench2Kg','Bench3Kg','Bench4Kg','Best3BenchKg','Deadlift1Kg','Deadlift2Kg','Deadlift3Kg','Deadlift4Kg','Best3DeadliftKg']
    for lift in lifts:
        session.add(Lift(name=lift))

    for row in lifting_data:
    # print(lifting_data[0])
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

        # book = (
        #     session.query(Book)
        #     .filter(Book.title == row["title"])
        #     .one_or_none()
        # )
        # if book is None:
        #     book = Book(title=row["title"])
        #     session.add(book)

        # publisher = (
        #     session.query(Publisher)
        #     .filter(Publisher.name == row["publisher"])
        #     .one_or_none()
        # )
        # if publisher is None:
        #     publisher = Publisher(name=row["publisher"])
        #     session.add(publisher)

        # # add the items to the relationships
        # author.books.append(book)
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
