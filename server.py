"""
Base file.
Instances the server and instances renderings
"""

from flask import render_template
from flask import request
import config
import os
import signal

# get the connexion app instance from config file
# to avoid calling it from config each time
conn_app = config.conn_app

# configure API endpoints with swagger file
conn_app.add_api('swagger.yml')

# creathe the base URL route
@conn_app.route('/')
def home():
	"""
	Base page for the app
	response to localhost:5000/
	:return: rendered template 'home.html'
	"""
	return render_template('home.html')










@conn_app.route('/stopServer', methods=['GET'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return "Server is shutting down..."

if __name__ == "__main__":
	conn_app.run(debug=True)