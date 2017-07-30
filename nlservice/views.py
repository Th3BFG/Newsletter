from nlservice import app

@app.route('/')
@app.route('/index')
def index():
	# TODO: Show form to submit email
	return 'Hello World'
