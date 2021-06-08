from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


federation_meet = Table(
    "federation_meet",
    Base.metadata,
    Column("federation_id", Integer, ForeignKey("federation.federation_id")),
    Column("meet_id", Integer, ForeignKey("meet.meet_id")),
)

location_meet = Table(
    "location_meet",
    Base.metadata,
    Column("location_id", Integer, ForeignKey("location.location_id")),
    Column("meet_id", Integer, ForeignKey("meet.meet_id")),
)

athlete_lift = Table(
    "athlete_lift",
    Base.metadata,
    Column("athlete_id", Integer, ForeignKey("athlete.athlete_id")),
    Column("lift_id", Integer, ForeignKey("lift.lift_id")),
)

class Athlete_Info(Base):
    __tablename__ = "ahtlete_info"
    athlete_info_id = Column(Integer, primary_key=True)
    age = Column(Float)
    bodyweight = Column(Float)

class Athlete(Base):
    __tablename__ = "athlete"
    athlete_id = Column(Integer, primary_key=True)
    name = Column(String)
    lifts = relationship(
        "Lift", secondary=athlete_lift, back_populates="athletes"
    )

class Federation(Base):
    __tablename__ = "federation"
    federation_id = Column(Integer, primary_key=True)
    name = Column(String)
    meets = relationship(
        "Meet", secondary=federation_meet, back_populates="federations"
    )

class Lift(Base):
    __tablename__ = "lift"
    lift_id = Column(Integer, primary_key=True)
    name = Column(String)
    athletes = relationship(
        "Athlete", secondary=athlete_lift, back_populates="lifts"
    )

class Location(Base):
    __tablename__ = "location"
    location_id = Column(Integer, primary_key=True)
    country = Column(String)
    state = Column(String)
    town = Column(String)
    meets = relationship(
        "Meet", secondary=location_meet, back_populates="locations"
    )

class Meet(Base):
    __tablename__ = "meet"
    meet_id = Column(Integer)
    name = Column(String)
    date = Column(String)
    key = Column(String, primary_key=True)
    federations = relationship(
        "Federation", secondary=federation_meet, back_populates="meets"
    )
    locations = relationship(
        "Location", secondary=location_meet, back_populates="meets"
    )