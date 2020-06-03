import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ['MONGO_INIT_ROOT_HOSTNAME'],
    27017)
db = client.tododb


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
