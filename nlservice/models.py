import datetime
from nlservice import db
from flask import jsonify

class Subscriber(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(120), index = True, unique = True)
	datesubbed = db.Column(db.String(12), index = True, unique = False)

	# Add a user to the database
	@staticmethod
	def add(address):
		date = str(datetime.date.today())
		sub = Subscriber(email = address, datesubbed = date)
		# TODO: Add error handling
		db.session.add(sub)
		db.session.commit()

	# Remove a user to the database
	@staticmethod
	def remove(address):
		sub = Subscriber.query.filter_by(email = address).first()
		if sub is not None:
			# TODO: Add error handling
			db.session.delete(sub)
			db.session.commit()

	# List all subscribers
	@staticmethod
	def list():
		# TODO: this will require a token check before making the query
		subs = Subscriber.query.all()
		# TODO: Return subscriber list as JSON
		text = ''
		for sub in subs:
			text += str(sub) +'<br/>'
		return text

	def __str__(self):
		return "%s subscribed on %s" % (self.email, self. datesubbed)
