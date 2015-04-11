from app import db
from db import Table, Column, Integer, ForeignKey, String, DateTime
from db.orm import relationship, backref

Base = declarative_base()

class Party(Base):
    """
    The object formerly known as Party, self explainitory
    """

    __tablename__ = 'party'

    id = db.column(db.Interger,primary_key=True)
    name = db.Column(db.String(128), index=True, unique= True)

    start_time  = db.Column(db.DateTime(timezone=True))
    end_time = db.Column(db.DateTime(timezone=True))

    location = db.Column(db.String(128))

    hosts = relationship("guests", order_by="guests.id")
    guests = relationship("Friend")


class Location(Base):
    """
    A location, this is where you party (verb)
    """

    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    entrances = relationship()

class Entrance(Base):
    """
    An entrance (Usually a door), the way people get into the party
    """

    __tablename__ = 'entrance'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    addr = db.Column(db.String())

class Friend(Base):
    """
    A friend, someone you enjoy spending time with and
    may invite to your party.
    """

    __tablename__ = 'friend'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),index= True, unique=True)

    contact_info = relationship("ContactInfo")

class ContactInfo(Base):
    """
    Contact Info, your means of getting your friends to the party
    """

    __tablename__ = 'contact_info'
    id = db.Column(db.Integer, primary_key=True)

    friend_id = relationship(Integer, ForeignKey(''))
    phone_numbers = db.Column(db.String(), index=True)
    email_address = db.Column(db.String(), index=True)
