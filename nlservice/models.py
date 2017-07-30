from nlservice import db

class Subscriber(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)
	datesubbed = db.Column(db.String(12), index=True, unique=False)

	def __repr__(self):
		return '<%r subscribed on %r>' % (self.email, self.datesubbed)
