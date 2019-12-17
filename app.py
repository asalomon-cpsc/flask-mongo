from os import environ
from datetime import datetime
from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os
import logging
import json


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['MONGO_URI'] = os.getenv('PROD_MONGODB')
mongo = PyMongo(app)


@app.route("/")
def index():

    result = []
    for report in mongo.db.report.find():
        result.append({'first_name': report['FirstName'],
                       'last_name': report['LastName'],
                       'email': report['Email'],
                       'state': report['State'],
                       'injury': report['Injury']})

    return jsonify(result)
