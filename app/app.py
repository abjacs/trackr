from flask import Flask, Request as request, Response, g
import sqlite3

import config


app = Flask(__file__)
app.config.from_object(config)


@app.before_request
def before_request():
	g.db = get_db_connection()

@app.after_request
def after_request(response):
	g.db.close()
	return response
	
@app.route("/")
def index():
	return "Hello"
	
@app.route("/update/<user_key>/<mac>", methods = ["GET", "POST"])
def update(user_key, mac):
	insert_query = "insert into tracks(userkey, mac) where userkey = %s values (?)" % (user_key)
	
	# DEBUG
	print insert_query
	
	g.db.execute(insert_query, [ mac ])
	g.db.commit()
	return "Username- %s at MAC- %s" % (user_key, mac)
	
def get_db_connection():
	return sqlite3.connect(app.config["DATABASE"])

if __name__ == "__main__":
	app.debug = True
	app.run("0.0.0.0")