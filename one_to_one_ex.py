from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/one_to_one_ex')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    passport = relationship("Passport", uselist = False, backref = "owner")

class Passport(Base):
    __tablename__ = 'passport'
    id = Column(Integer, primary_key = True)
    issue_date = Column(Date, nullable = False, default = datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('person.id'), nullable = False)

Base.metadata.create_all(engine)


chad = Person(name = "chad")
passport = Passport()
chad.passport = passport

session.add(chad)
session.commit()

print(chad.passport.issue_date)
print(passport.owner.name)