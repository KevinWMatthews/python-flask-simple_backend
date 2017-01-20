from flask import Blueprint, request, url_for, jsonify
from simple_backend import app

data_url_view = Blueprint('data_url', __name__)

UPLOAD_FOLDER = './data'
UPLOAD_FILENAME = 'update.file'

@app.route('/data_url', methods=['POST'])
def data_url():
    """
    # The original sample code listed the available files when
    # the user browsed to this url.
    # We aren't doing this, but I've retained and edited this for future use.
    # This returns javascript which the javascript/html could display nicely.
    # Before using this, import os and add GET to the list of methods for this URL.
    if request.method == 'GET':
        file_info = []
        file_names = os.listdir(UPLOAD_FOLDER)
        for file_name in file_names:
            file_info.append(dict(name = file_name))

        return jsonify(files=file_info)
    """

    # Save the uploaded file and return a flask Response() that contains json with file details.
    # Return whatever json the uploadl.html javascript expects.
    if request.method == 'POST':
        # The uploaded file is accessible an ImmutableMultiDict that contains a FileStorage object.
        # For documentation on this object, see
        # http://mitsuhiko.pocoo.org/werkzeug-docs/utils.html
        # and search for werkzeug.FileStorage
        data_file = request.files.get('upload_file')        # The name from the html fileupload input
        file_name = data_file.filename

        #TODO verify file extension, etc.

        data_file.save('%s/%s' % (UPLOAD_FOLDER, UPLOAD_FILENAME))  # buffer_size defautls to 16384

        # jsonify wraps the arguments in json and returns a flask.Response() object. Use this!
        # For documentation on this object, see
        # http://flask.pocoo.org/docs/0.12/api/#flask.Response
        return jsonify(name = file_name)
