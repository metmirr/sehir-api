from flask import jsonify, request, url_for
from .. import db
from ..models import City

from . import api


@api.route('/cities/')
def get_cities():
    cities = City.query.all()
    return jsonify([city.to_json() for city in cities])

@api.route('/city/<int:id>')
def get_city(id):
    city = City.query.get_or_404(id)
    return jsonify(city.to_json())
