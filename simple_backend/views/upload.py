from flask import render_template, Blueprint, abort
from jinja2 import TemplateNotFound
from simple_backend import app

upload_view = Blueprint('upload', __name__)

@app.route('/upload')
def upload():
    try:
        return render_template('upload.html')
    except TemplateNotFound:
        abort(404)
