from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os

from extensions import db, migrate
from resources.boards import Boards
from resources.tags import Tags


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))

    register_extensions(app)

    return app


if __name__ == '__main__':
    app = create_app()

    api = Api(app)
    api.add_resource(Boards, '/boards')
    api.add_resource(Tags, '/tags')

    app.run(host= "0.0.0.0",port="5000")
