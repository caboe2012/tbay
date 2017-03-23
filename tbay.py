from sqlalchemy import Column, Integer, Date, String, DateTime, Float, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    description = Column(String)
    start_time = Column(DateTime, default = datetime.utcnow)
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    bids = relationship("Bid", backref = "items")
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    username = Column(String, nullable = False)
    password = Column(String, nullable = False)
    
    auction_items = relationship("Item", backref = "users")
    bids = relationship("Bid", backref = "users")
    #bids = relationship("Bid", backref = "bids_user")
    #bid_ids = Column(Integer, ForeignKey('bids.id'))# nullable = False)
    
class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key = True)
    price = Column(Float, nullable = False)
    
    item_id = Column(Integer, ForeignKey('items.id'))#, nullable = False)
    user_id = Column(Integer, ForeignKey('users.id'))#, nullable = False)

Base.metadata.create_all(engine)