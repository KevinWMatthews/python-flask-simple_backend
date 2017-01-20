from flask import render_template, Blueprint, abort, request, url_for, jsonify
from jinja2 import TemplateNotFound
from simple_backend import app

data_url_view = Blueprint('data_url', __name__)

UPLOAD_FOLDER = './data'
UPLOAD_FILENAME = 'update.file'

#  if 'coffee.jpg' not in request.files:
#  print 'POST request does not contain file!'
#TODO  this return shouldn't return anything?
#  return '<html><body>data_url html</body></html'   #render_template('upload.html')   # ?

#  if file.filename == '':
#  print 'file has no filename!'
#  return '<html><body>data_url html</body></html'   #render_template('upload.html')   # ?

@app.route('/data_url', methods=['POST', 'GET'])
def data_url():
    if request.method == 'GET':
        # we are expected to return a list of dicts with infos about the already available files:
        file_infos = []
        for file_name in list_files():
            file_url = url_for('download', file_name=file_name)
            file_size = get_file_size(file_name)
            file_infos.append(dict(name=file_name,
                                   size=file_size,
                                   url=file_url))
        return jsonify(files=file_infos)

    if request.method == 'POST':
        # we are expected to save the uploaded file and return some infos about it:
        #                              vvvvvvvvv   this is the name for input type=file
        print request.files
        data_file = request.files.get('files[]')
        file_name = data_file.filename

        print data_file.filename
        # print data_file.stream
        print data_file.content_type
        content_length = data_file.content_length
        print content_length
        data_file.save('%s/%s' % (UPLOAD_FOLDER, UPLOAD_FILENAME))     # buffer_size=16384
        print data_file.content_length

        # save_file(data_file, file_name)
        # file_size = get_file_size(file_name)
        file_size = 42
        file_url = url_for('upload', file_name=file_name)   #download
        # providing the thumbnail url is optional
        # thumbnail_url = url_for('thumbnail', file_name=file_name)
        return jsonify(name=file_name,
                       size=file_size,
                       url=file_url)#,
                       #thumbnail=thumbnail_url)
