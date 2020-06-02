import os
import time
import datetime
import logging
import flask
import werkzeug
import tornado.wsgi
import tornado.httpserver
import numpy as np
from PIL import Image
import urllib

from skimage import io, transform, exposure
from demo_new import *

UPLOAD_FOLDER = 'static/upload'
RESULT_FOLDER = 'static/result'
ALLOWED_IMAGE_EXTENSIONS = set(['png', 'bmp', 'jpg', 'jpeg'])

# Obtain the flask app object
app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index3.html', has_result=False)

@app.route('/trans1', methods=['POST'])
def trans1():
    try:
        # We will save the file to disk for possible data collection.
        imf = flask.request.form['image']
        filename_ = str(time.time()).replace('.', '_') + '.png'
#        filename_ = 'tmp.jpg'
        filename = os.path.join(UPLOAD_FOLDER, filename_)
        filename2 = os.path.join(RESULT_FOLDER, filename_)
        imf = base64.b64decode(imf)
        with open(filename, "wb") as f:
            f.write(imf)
        im = io.imread(filename)
        im = transform.resize(im, [512,512])
        io.imsave(filename, im)
        logging.info('Saving to %s.', filename)
        input_pic(filename, filename2)

    except Exception as err:
        logging.info('Uploaded image open error: %s', err)
        return flask.render_template(
            'index3.html', has_result=True,
            result=(False, 'Cannot open uploaded image.')
        )

    return json.dumps({"image2":filename2})

@app.route('/trans2', methods=['POST'])
def trans2():
    try:
        # We will save the file to disk for possible data collection.
        imf = flask.request.form['image']
        filename_ = str(time.time()).replace('.', '_') + '.png'
#        filename_ = 'tmp.jpg'
        filename = os.path.join(UPLOAD_FOLDER, filename_)
        filename2 = os.path.join(RESULT_FOLDER, filename_)
        imf = base64.b64decode(imf)
        with open(filename, "wb") as f:
            f.write(imf)
        im = io.imread(filename)
        im = transform.resize(im, [512,512])
        io.imsave(filename, im)
        logging.info('Saving to %s.', filename)
        input_pic2(filename, filename2)

    except Exception as err:
        logging.info('Uploaded image open error: %s', err)
        return flask.render_template(
            'index3.html', has_result=True,
            result=(False, 'Cannot open uploaded image.')
        )

    return json.dumps({"image2":filename2})

@app.route('/trans3', methods=['POST'])
def trans3():
    try:
        # We will save the file to disk for possible data collection.
        imf = flask.request.form['image']
        filename_ = str(time.time()).replace('.', '_') + '.png'
#        filename_ = 'tmp.jpg'
        filename = os.path.join(UPLOAD_FOLDER, filename_)
        filename2 = os.path.join(RESULT_FOLDER, filename_)
        imf = base64.b64decode(imf)
        with open(filename, "wb") as f:
            f.write(imf)
        im = io.imread(filename)
        im = transform.resize(im, [512,512])
        io.imsave(filename, im)
        logging.info('Saving to %s.', filename)
        input_pic3(filename, filename2)

    except Exception as err:
        logging.info('Uploaded image open error: %s', err)
        return flask.render_template(
            'index3.html', has_result=True,
            result=(False, 'Cannot open uploaded image.')
        )

    return json.dumps({"image2":filename2})
 

@app.route('/sketchify', methods=['POST'])
def sketchify2():
    try:
        # We will save the file to disk for possible data collection.
        imf = flask.request.form['image']
        filename_ = str(time.time()).replace('.', '_') + '.png'
#        filename_ = 'tmp.jpg'
        filename = os.path.join(UPLOAD_FOLDER, filename_)
        filename2 = os.path.join(RESULT_FOLDER, filename_)
        imf = base64.b64decode(imf)
        with open(filename, "wb") as f:
            f.write(imf)
        im = io.imread(filename)
        im = transform.resize(im, [512,512])
        io.imsave(filename, im)
        logging.info('Saving to %s.', filename)
        sketchify(filename, filename2)

    except Exception as err:
        logging.info('Uploaded image open error: %s', err)
        return flask.render_template(
            'index3.html', has_result=True,
            result=(False, 'Cannot open uploaded image.')
        )

    return json.dumps({"image1":filename2})



def allowed_file(filename):
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1] in ALLOWED_IMAGE_EXTENSIONS
    )


def start_tornado(app, port=5001):
    http_server = tornado.httpserver.HTTPServer(
        tornado.wsgi.WSGIContainer(app))
    http_server.listen(port)
    print("Tornado server starting on port {}".format(port))
    tornado.ioloop.IOLoop.instance().start()


def start_from_terminal(app):
    """
    Parse command line options and start the server.
    """

#     app.run(debug=True, host='0.0.0.0', port=5000)
    start_tornado(app, port=10086)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    start_from_terminal(app)


