from flask.ext.sqlalchemy import SQLAlchemy
db =  SQLAlchemy()

class Party(db.Model):
    """
    The object formerly known as Party, self explanatory
    """
    __tablename__ = 'party'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128), index=True, unique= True)
    start_time  = db.Column(db.DateTime(timezone=True))
    end_time = db.Column(db.DateTime(timezone=True))
    party_loc = db.Column(db.Integer, db.ForeignKey("location.id"))
    invitation = db.relationship("Invitation", backref="party")


class Invitation(db.Model):
    """
    An invitation, your golden ticket to the best night ever"
    """
    __tablename__ = 'invitation'
    id = db.Column(db.Integer, primary_key=True)
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'))
    friend_inv =  db.Column(db.Integer, db.ForeignKey('friend.id'))
    remaining_invites = db.Column(db.Integer())

    def __init__(self, party, friend):
        self.party = party
        self.friend = friend
        self.remaining_invites = 4


class Location(db.Model):
    """
    A location, this is where you party (verb)
    """
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    parties_here = db.relationship("Party", backref="location")
    entrances = db.relationship("Entrance", backref="location")

class Entrance(db.Model):
    """
    An entrance (Usually a door), the way people get into the party
    """
    __tablename__ = 'entrance'
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    name = db.Column(db.String())
    addr = db.Column(db.String())

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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),index= True, unique=True)
    contact_info = db.relationship("ContactInfo")
    friend_inv  = db.relationship("Invitation", backref="friend")


class ContactInfo(db.Model):
    """
    Contact Info, your means of getting your friends to the party
    """
    __tablename__ = 'contact_info'
    id = db.Column(db.Integer, primary_key=True)
    friend_id = db.Column(db.Integer, db.ForeignKey('friend.id'))
    phone_numbers = db.Column(db.String(), index=True)
    email_address = db.Column(db.String(), index=True)

