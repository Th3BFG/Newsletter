from flask import render_template, flash, redirect
from nlservice import app
from .forms import SubscribeForm, UnsubscribeForm
from .models import Subscriber

# Main/index endpoint for Subscribe form
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
	form = SubscribeForm()
	# Verify that the form has been filled out
	if form.validate_on_submit():
		# TODO: Better confirmation for sub
		#flash('Attempting to subscribe "%s" to the mailing list.' % (form.email.data))
		Subscriber.add(form.email.data)
		return "User Subscribed"
	else:
		return render_template('subscribe.html', title = 'Subscribe', form = form)

# Remove a user from the subscriber list
@app.route('/unsubscribe', methods = ['GET', 'POST'])
def unsubscribe():
	form = UnsubscribeForm()
	if form.validate_on_submit():
		# TODO: Better confirmation of removal
		Subscriber.remove(form.email.data)
		return "User Unsubscribed"
	else:
		return render_template('unsubscribe.html', title = 'Unsubscribe', form = form)

# Returns the list of subscribers
@app.route('/list', methods = ['GET'])
def list():
	# TODO: this will need a token so that external users cannot leverage it
	return Subscriber.list()

