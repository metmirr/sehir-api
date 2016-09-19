from datetime import datetime
from . import db
from flask import url_for
from .citiesdict import cities

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    city_code = db.Column(db.Integer, index=True, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<City %s>' % self.name

    def to_json(self):
        json_city = {
                'URL': url_for('api.get_city', id=self.id, _external=True),
                'Sehir-Bilgileri': {
                    'plaka': self.city_code,
                    'sehir': self.name,
                }
                'Eklendi': self.timestamp,
                'Google Map Link': 'https://www.google.com/maps/place/{}'.format(self.name),
        }
        return json_city
    @staticmethod
    def insert_cities():
        for c in cities:
            city = City.query.filter_by(name=c['name']).first()
            if city is None:
                city = City(name=c['name'], city_code=c['city_code'])
            db.session.add(city)
            db.session.commit()