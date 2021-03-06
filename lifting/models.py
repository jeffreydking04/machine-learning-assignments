from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# federation_meet = Table(
#     "federation_meet",
#     Base.metadata,
#     Column("federation_id", Integer, ForeignKey("federation.federation_id")),
#     Column("meet_id", Integer, ForeignKey("meet.meet_id")),
# )

# location_meet = Table(
#     "location_meet",
#     Base.metadata,
#     Column("location_id", Integer, ForeignKey("location.location_id")),
#     Column("meet_id", Integer, ForeignKey("meet.meet_id")),
# )

class Athlete(Base):
    __tablename__ = "athlete"
    athlete_id = Column(Integer, primary_key=True)
    name = Column(String)
    lifts = relationship("Lift", backref=backref("athlete"))

class Federation(Base):
    __tablename__ = "federation"
    federation_id = Column(Integer, primary_key=True)
    name = Column(String)
    lifts = relationship("Lift", backref=backref("federation"))
    meets = relationship("Meet", backref=backref("federation"))
    # meets = relationship(
    #     "Meet", secondary=federation_meet, back_populates="federations"
    # )

class Lift(Base):
    __tablename__ = "lift"
    lift_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey("athlete.athlete_id"))
    location_id = Column(Integer, ForeignKey("location.location_id"))
    federation_id = Column(Integer, ForeignKey("federation.federation_id"))
    meet_id = Column(Integer, ForeignKey("meet.meet_id"))
    lift_id = Column(Integer, primary_key=True)
    athlete_age = Column(Float)
    athlete_weight = Column(Float)
    squat_1_kg = Column(Float)    
    squat_2_kg = Column(Float)    
    squat_3_kg = Column(Float)    
    squat_4_kg = Column(Float)    
    best_3_squat_kg = Column(Float)    
    bench_1_kg = Column(Float)    
    bench_2_kg = Column(Float)    
    bench_3_kg = Column(Float)    
    bench_4_kg = Column(Float)    
    best_3_bench_kg = Column(Float)    
    deadlift_1_kg = Column(Float)    
    deadlift_2_kg = Column(Float)    
    deadlift_3_kg = Column(Float)    
    deadlift_4_kg = Column(Float)    
    best_3_deadlift_kg = Column(Float)

class Location(Base):
    __tablename__ = "location"
    location_id = Column(Integer, primary_key=True)
    country = Column(String)
    state = Column(String)
    town = Column(String)
    lifts = relationship("Lift", backref=backref("location"))
    meets = relationship("Meet", backref=backref("location"))
    # meets = relationship(
    #     "Meet", secondary=location_meet, back_populates="locations"
    # )

class Meet(Base):
    __tablename__ = "meet"
    meet_id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey("location.location_id"))
    federation_id = Column(Integer, ForeignKey("federation.federation_id"))
    name = Column(String)
    date = Column(String)
    key = Column(String)
    lifts = relationship("Lift", backref=backref("meet"))
    # federations = relationship(
    #     "Federation", secondary=federation_meet, back_populates="meets"
    # )
    # locations = relationship(
    #     "Location", secondary=location_meet, back_populates="meets"
    # )