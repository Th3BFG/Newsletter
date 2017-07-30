import datetime
from nlservice import db

class Subscriber(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)
	datesubbed = db.Column(db.String(12), index=True, unique=False)

	# Add a user to the database
	@staticmethod
	def add(address):
		date = str(datetime.date.today())
		sub = Subscriber(email = address, datesubbed = date)
		# TODO: Add error handling
		db.session.add(sub)
		db.session.commit()

	# List all subscribers
	@staticmethod
	def list():
		subs = Subscriber.query.all()
		text = ''
		for sub in subs:
			text += sub.email + ' '
		return text

	def __repr__(self):
		return '<%r subscribed on %r>' % (self.email, self.datesubbed)
