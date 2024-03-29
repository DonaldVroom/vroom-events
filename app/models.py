from app import db
from datetime import datetime

class QteamEvent(db.Model):
    __tablename__ = 'qteamevent'

    id = db.Column(db.Integer, primary_key=True)
    how_many_centers = db.Column(db.String(), nullable=False)
    which_type_car = db.Column(db.String(), nullable=False)
    when_summer_tires = db.Column(db.String(), nullable=False)
    how_many_people = db.Column(db.Integer(), nullable=False)
    email = db.Column(db.String())
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    locale = db.Column(db.String(10))

    def __repr__(self):
        return f"<QteamEvent {self.id}>"
    
class QteamEvent2(db.Model):
    __tablename__ = 'qteamevent2'

    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.String(), nullable=False)
    q2 = db.Column(db.String(), nullable=False)
    q3 = db.Column(db.String(), nullable=False)
    q4 = db.Column(db.Integer(), nullable=False)
    how_many_people = db.Column(db.Integer(), nullable=False)
    email = db.Column(db.String())
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    phone = db.Column(db.String())
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    locale = db.Column(db.String(10))

    def __repr__(self):
        return f"<QteamEvent2 {self.id}>"

class SuzukiLead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auto = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    locale = db.Column(db.String(10))

    def __repr__(self):
        return f"<SuzukiLead {self.id}>"
    
class FordBroncoEvent(db.Model):
    __tablename__ = 'fordbroncoevent'

    id = db.Column(db.Integer, primary_key=True)
    first_generation = db.Column(db.String(), nullable=False)
    goat_meaning = db.Column(db.String(), nullable=False)
    famous_person = db.Column(db.String(), nullable=False)
    how_old = db.Column(db.String(), nullable=False)
    towing_capacity = db.Column(db.String(), nullable=False)
    total_gears = db.Column(db.String(), nullable=False)
    how_many_people = db.Column(db.Integer(), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String())
    phone = db.Column(db.String())
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    locale = db.Column(db.String(10))

    def __repr__(self):
        return f"<QteamEvent {self.id}>"
    

class VwCupEvent(db.Model):
    __tablename__ = 'vwcupevent'

    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.String(), nullable=False)
    q2 = db.Column(db.String(), nullable=False)
    how_many_people = db.Column(db.Integer(), nullable=False)
    email = db.Column(db.String())
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    phone = db.Column(db.String())
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    locale = db.Column(db.String(10))
    postal_code = db.Column(db.String(10))
    dob = db.Column(db.DateTime)

    def __repr__(self):
        return f"<vwcupevent {self.id}>"