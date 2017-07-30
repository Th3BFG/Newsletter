from flask import render_template, flash, redirect
from nlservice import app
from .forms import SubscribeForm
from .models import Subscriber

# Main/index endpoint for Subscribe form
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = SubscribeForm()
	# Verify that the form has been filled out
	if form.validate_on_submit():
		# TODO: Better confirmation for sub
		#flash('Attempting to subscribe "%s" to the mailing list.' % (form.email.data))
		Subscriber.add(form.email.data)
		return "User Subscribed"
	else:
		return render_template('subscribe.html', title='Subscribe', form=form)

# Returns the list of subscribers
@app.route('/list', methods=['GET']) # GET by default
def list():
	# TODO: this will need a token so that external users cannot leverage it
	return Subscriber.list()
	
