from flask import render_template, Blueprint
from simple_backend import app

upload_view = Blueprint('upload', __name__)

@app.route('/upload')
def upload():
    return render_template('upload.html')
