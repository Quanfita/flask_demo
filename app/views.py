from flask.views import MethodView
from flask import make_response, render_template

import json

class IndexView(MethodView):

    def get(self):
        return render_template('index.html')
    
    def post(self):
        return make_response('')
