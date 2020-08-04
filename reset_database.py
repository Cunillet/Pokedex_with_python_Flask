import os
from config import db
from models import Pokemon

POKEMONS = [
	{
		'pokemon_id': 25,
		'name':'Pokachu',
		'ptype': 'electric',
		'weight': 6.0,
		'height': 0.4,
	},
	{
		'pokemon_id': 1,
		'name':'Bulbasaur',
		'ptype': 'plant',
		'weight': 6.9,
		'height': 0.7,
	},
	{
		'pokemon_id': 4,
		'name':'Charmander',
		'ptype': 'fire',
		'weight': 8.5,
		'height': 0.6,
	},
	{
		'pokemon_id': 7,
		'name':'Squirtle',
		'ptype': 'water',
		'weight': 9.0,
		'height': 0.5,
	}
]

# Delete DB if exist to restart
if os.path.exists('pokemons.db'):
	os.remove('pokemons.db')

# create the database
db.create_all()

for p in POKEMONS:
	pokemon = Pokemon(pokemon_id=p['pokemon_id'], name=p['name'], ptype=p['ptype'], weight=p['weight'], height=p['height'])
	db.session.add(pokemon)

db.session.commit()