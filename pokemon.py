"""
Pokemon module that supports all REST actions from
pokemon data
"""

from flask import make_response, abort
from config import db
from models import Pokemon, PokemonSchema

def read_all():
	"""
	complete list of available pokemons
	:request: /api/pokemon
	:return: json string of list of pokemons
	"""
	# request data using the model
	pokemons = Pokemon.query.order_by(Pokemon.pokemon_id).all()

	# serialize the data from the response
	pokemons_schema = PokemonSchema(many=True)
	data = pokemons_schema.dump(pokemons)
	return data