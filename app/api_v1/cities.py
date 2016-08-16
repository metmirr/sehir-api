from flask import jsonify, request, url_for, abort
from .. import db
from ..models import City

from . import api


@api.route('/cities/')
def get_cities():
    cities = City.query.all()
    return jsonify([city.to_json() for city in cities])

@api.route('/city/<int:id>')
@api.route('/city/<name>')
def get_city(id=None, name=None):
	if id is not None:
		city = City.query.get_or_404(id)
	if name is not None:
		name = name.capitalize()
		city = City.query.filter_by(name=name).first()
		if city is None:
			abort(404)
	return jsonify(city.to_json())

