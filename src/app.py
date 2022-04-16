from flask import Flask, jsonify
from flask_restful import Resource, Api, abort, reqparse
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
db = SQLAlchemy(app)
api = Api(app)

from resources.maquinas import Maquinas

api.add_resource(Maquinas, '/maquinas')

if __name__ == '__main__':
    app.run()