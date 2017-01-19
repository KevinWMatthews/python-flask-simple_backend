from flask import render_template, Blueprint, abort, request
from jinja2 import TemplateNotFound
from simple_backend import app

data_url_view = Blueprint('data_url', __name__)

@app.route('/data_url', methods=['POST', 'GET'])
def data_url():
    try:
        print 'In data_url.py, %s' % request.method
        return '<html><body>data_url html</body></html'   #render_template('data_url.html')
    except TemplateNotFound:
        abort(404)
