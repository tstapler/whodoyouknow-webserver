from app import db
from db import Table, Column, Integer, ForeignKey, String, DateTime
from db.orm import relationship, backref

Base = declarative_base()

class Party(Base):
    """
    The object formerly known as Party, self explanatory
    """
    __tablename__ = 'party'
    id = column(Interger,primary_key=True)
    name = Column(String(128), index=True, unique= True)
    start_time  = Column(DateTime(timezone=True))
    end_time = Column(DateTime(timezone=True))
    location = Column(Integer, ForeignKey("location.id"))
    invitations = relationship("Invitation", backref="party")


class Invitation(Base):
    """
    An invitation, your golden ticket to the best night ever"
    """
    __tablename__ = 'invitation'
    id = Column(Integer, primary_key=True)
    party = Column(Integer, ForeignKey('party.id'))
    friend =  Column(Integer, ForeignKey('friend.id'))


class Location(Base):
    """
    A location, this is where you party (verb)
    """
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String())
    parties = relationship("Party", backref="location")
    entrances = relationship("Entrance", backref="location")


class Entrance(Base):
    """
    An entrance (Usually a door), the way people get into the party
    """
    __tablename__ = 'entrance'
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('location.id'))
    name = Column(String())
    addr = Column(String())


class Friend(Base):
    """
    A friend, someone you enjoy spending time with and
    may invite to your party.
    """
    __tablename__ = 'friend'
    id = Column(Integer, primary_key=True)
    name = Column(String(128),index= True, unique=True)
    contact_info = relationship("ContactInfo", backref="friend")
    invitations = relationship("Invitation")

class ContactInfo(Base):
    """
    Contact Info, your means of getting your friends to the party
    """
    __tablename__ = 'contact_info'
    id = Column(Integer, primary_key=True)
    friend_id = Column(Integer, ForeignKey('friend.id'))
    phone_numbers = Column(String(), index=True)
    email_address = Column(String(), index=True)

