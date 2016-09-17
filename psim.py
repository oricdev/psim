# coding=utf-8
# !flask/bin/python
# code for flask REST API copied and adapted from:
#  http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
from __future__ import division

import os
from flask import Flask, jsonify, render_template, request

# from numpy import pi
# import numpy

# ##########################
# ENTRY POINT FOR THE CODE #
# ##########################
print "Starting Psim.."

# setting up template directory and location of local resources for Flask
# here : http://www.html5rocks.com/en/tutorials/webcomponents/imports/
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), './resources')
app = Flask(__name__, static_folder=ASSETS_DIR)
# app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/todo/', methods=['GET'])
def get_task():
    ret_data = {"value": request.args.get('id')}
    print request.args.get('id')
    return jsonify(ret_data)


@app.route('/getslotsdata/', methods=['GET'])
def getNextSlotsData():
    timeGap = {"value": request.args.get('timegap')}
    nbSlotsToGet = {"value": request.args.get('nbslots')}


if __name__ == '__main__':
    app.run(debug=True)

