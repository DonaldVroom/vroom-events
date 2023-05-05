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

    def __repr__(self):
        return f"<QteamEvent {self.id}>"

class SuzukiLead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auto = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    salutation = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<SuzukiLead {self.id}>"