from config import db
from marshmallow_sqlalchemy import ModelSchema

class Pokemon(db.Model):
	__tablename__ = 'pokemon'
	pokemon_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))
	ptype = db.Column(db.String(32))
	weight = db.Column(db.Float)
	height = db.Column(db.Float)

class PokemonSchema(ModelSchema):
	class Meta:
		model = Pokemon
		sqla_session = db.session

