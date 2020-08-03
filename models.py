from config import db, ma
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Pokemon(db.Model):
	__tablename__ = 'pokemon'
	pokemon_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32))
	description = db.Column(db.String(256))
	ptype = db.Column(db.String(32))
	weight = db.Column(db.Integer)
	height = db.Column(db.Integer)
	sound = db.Column(db.String(32))

class PokemonSchema(ModelSchema):
	def __init__(self, **kwargs):
		super().__init__(strict=True, **kwargs)

	class Meta:
		model = Pokemon
		sqla_session = db.session