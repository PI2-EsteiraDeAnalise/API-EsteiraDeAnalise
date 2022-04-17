from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os

from extensions import db
from resources.maquinas import Maquinas


def register_extensions(app):
    db.init_app(app)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)

    return app


if __name__ == '__main__':
    app = create_app(os.getenv('APP_SETTINGS'))

    api = Api(app)
    api.add_resource(Maquinas, '/maquinas')

    app.run()
