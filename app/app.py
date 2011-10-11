from flask import Flask
import sqlite3

import config


app = Flask(__file__)
app.config.from_object(config)

"""
@app.before_request
def before_request():
	g.connection = config.get_db_connection()

@app.after_request
def after_request():
	g.connection.close()
"""
	
@app.route("/")
def index():
	return "Hello"

def get_db_connection():
	return sqlite3.connect(app.config["DATABASE"])

if __name__ == "__main__":
	app.run("0.0.0.0")