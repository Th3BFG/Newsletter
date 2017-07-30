from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask instance and set config
app = Flask(__name__)
app.config.from_object('config')
# Make DB connection
db = SQLAlchemy(app)

# import at the end to avoid a circular reference
from nlservice import views, models
