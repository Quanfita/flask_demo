import flask_restful
from flask import Flask
import os
from flask_cors import *

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
api = flask_restful.Api(app)
CORS(app, supports_credentials=True)
