from os import environ
from datetime import datetime
from pymongo import MongoClient
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os
import logging
import json


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
mongo_conn_str = os.getenv('PROD_MONGODB')


@app.route("/")
def index():
    # try:
    # write to DB
    mClient = MongoClient(mongo_conn_str)
    # get db
    db = mClient.neiss_test
    result = []
    for report in db.report.find():
        result.append(report)
 # except Exception:
        # call this method if any of the database operation above fail
    return jsonify(report)
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
