from app import db
from db import Table, Column, Integer, ForeignKey, String, DateTime
from db.orm import relationship, backref

db.Model = declarative_base()

class Party(db.Model):
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

    def __init__(self, name, start_time, end_time, location):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location


class Invitation(db.Model):
    """
    An invitation, your golden ticket to the best night ever"
    """
    __tablename__ = 'invitation'
    id = Column(Integer, primary_key=True)
    party = Column(Integer, ForeignKey('party.id'))
    friend =  Column(Integer, ForeignKey('friend.id'))
    remaining_invites = Column(Integer())

    def __init__(self, party, friend):
        self.party = party
        self.friend = friend
        self.remaining_invites = 4


class Location(db.Model):
    """
    A location, this is where you party (verb)
    """
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String())
    parties = relationship("Party", backref="location")
    entrances = relationship("Entrance", backref="location")

    def __init__(self, name):
        self.name = name


class Entrance(db.Model):
    """
    An entrance (Usually a door), the way people get into the party
    """
    __tablename__ = 'entrance'
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('location.id'))
    name = Column(String())
    addr = Column(String())

    def __init__(self, location_id, name, addr):
        self.location_id = location_id
        self.name = name
        self.addr = addr


class Friend(db.Model):
    """
    A friend, someone you enjoy spending time with and
    may invite to your party.
    """
    __tablename__ = 'friend'
    id = Column(Integer, primary_key=True)
    name = Column(String(128),index= True, unique=True)
    contact_info = relationship("ContactInfo", backref="friend")
    invitations = relationship("Invitation", backref="friend")

    def __init__(self, name):
        self.name = name


class ContactInfo(db.Model):
    """
    Contact Info, your means of getting your friends to the party
    """
    __tablename__ = 'contact_info'
    id = Column(Integer, primary_key=True)
    friend_id = Column(Integer, ForeignKey('friend.id'))
    phone_numbers = Column(String(), index=True)
    email_address = Column(String(), index=True)

