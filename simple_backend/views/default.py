from flask import render_template, Blueprint
from simple_backend import app

default_view = Blueprint('index', __name__)

@app.route('/', defaults={'page': 'index'})
@app.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
