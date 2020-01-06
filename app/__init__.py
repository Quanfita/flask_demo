# -*- encoding: utf-8 -*-
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#import config

#db = SQLAlchemy()
from app.flask_app import app
from app.views import IndexView

app.add_url_rule('/index/',view_func=IndexView.as_view('index'))
