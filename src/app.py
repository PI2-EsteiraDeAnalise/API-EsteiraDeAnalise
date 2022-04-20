from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os

from extensions import db
from resources.placas import Placas


def register_extensions(app):
    db.init_app(app)


def create_app(config):
    app = Flask(__name__)
    print("setting: ", config)
    app.config.from_object(config)

    register_extensions(app)

    return app


if __name__ == '__main__':
    print("setting: ", os.getenv('APP_SETTINGS'))
    app = create_app(os.getenv('APP_SETTINGS'))

    api = Api(app)
    api.add_resource(Placas, '/placas')

    app.run(host= "0.0.0.0",port="5000")
