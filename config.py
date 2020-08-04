import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# create the connexion application instance
conn_app = connexion.App(__name__, specification_dir=basedir)

# gets the flask app instance
app = conn_app.app

# build the SQLite URL for SQLAlchemy
sqlite_url = 'sqlite:///' + os.path.join(basedir, 'pokemons.db')

# configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create the SQLAlchemy DB instance
db = SQLAlchemy(app)

# instance marshmallow
ma = Marshmallow(app)
