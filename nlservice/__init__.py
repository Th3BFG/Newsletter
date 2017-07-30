from flask import Flask

app = Flask(__name__)
# import at the end to avoid a circular reference
from nlservice import views
