from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

from extensions import db, migrate

from resources.boards import Boards
from resources.tags import Tags
from resources.metrics import Metrics
from resources.coordinates import Coordinates
from resources.coordinate import Coordinate


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv("APP_SETTINGS"))

    register_extensions(app)

    CORS(app)

    return app


if __name__ == "__main__":
    app = create_app()

    api = Api(app)

    api.add_resource(Boards, "/boards")
    api.add_resource(Tags, "/tags")
    api.add_resource(Metrics, "/metrics")
    api.add_resource(Coordinates, "/coordinates")
    api.add_resource(Coordinate, "/coordinate/<record_id>")

    app.run(host="0.0.0.0", port="5000")
