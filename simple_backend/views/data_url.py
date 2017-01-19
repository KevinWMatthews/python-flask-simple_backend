from flask import render_template, Blueprint, abort, request
from jinja2 import TemplateNotFound
from werkzeug.datastructures import ImmutableMultiDict
from simple_backend import app

data_url_view = Blueprint('data_url', __name__)

UPLOAD_FOLDER = '~'

#  if 'coffee.jpg' not in request.files:
#  print 'POST request does not contain file!'
#TODO  this return shouldn't return anything?
#  return '<html><body>data_url html</body></html'   #render_template('upload.html')   # ?

#  if file.filename == '':
#  print 'file has no filename!'
#  return '<html><body>data_url html</body></html'   #render_template('upload.html')   # ?

@app.route('/data_url', methods=['POST', 'GET'])
def data_url():
    if request.method == 'POST':
        print request.files
        # The js in the html sets 'dataType' to 'json', so we should return json.
        #  return 42
        #  return '{ error:0,name:"bob"}'
        #  return 'success'
        #  return '{readyState: 4, responseText: "success", status: 200, statusText: "OK"}'
        #  return '<html><body>data_url html</body></html'   #render_template('upload.html')
        #  return '{ files: [ { error: 0, name: "thumb2.jpg", } ] }'
        return '{ error:0, length:42 }'

    try:
        print 'In data_url.py, %s' % request.method
        return '<html><body>data_url html</body></html'   #render_template('upload.html')
    except TemplateNotFound:
        abort(404)
