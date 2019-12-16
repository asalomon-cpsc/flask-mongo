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
    # try:
    # write to DB
    # get db

    result = []
    for report in mongo.db.report.find():
        print(report)
        result.append(report)
 # except Exception:
        # call this method if any of the database operation above fail
    return report
 # finally:
   # print('Process completed')


#serve(app, host="0.0.0.0", port='5000')

# if __name__ == '__main__':
#   HOST = environ.get('SERVER_HOST', '0.0.0.0')
#   try:
#       PORT = int(environ.get('SERVER_PORT', '5555'))
#  except ValueError:
#      PORT = 5555
#   app.run(HOST, PORT)
