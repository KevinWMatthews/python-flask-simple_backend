from flask import render_template, Blueprint
from simple_backend import app

index_page = Blueprint('index', __name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
