from flask_restful import Resource
from flask import jsonify, request

from extensions import db
from models.coordinate import Coordinate


class Coordinates(Resource):
    def get(self):
        records = Coordinate.query.all()

        if len(records) == 0:
            return make_response(
                jsonify({"message": "Nenhum registro encontrado"}), 404
            )

        return make_response(
            jsonify([Coordinate.serialize(record) for record in records]), 200
        )

    def post(self):
        args = request.get_json()

        coordinate_record = Coordinate(id=args["id"], tag=args["tag"])

        db.session.add(coordinate_record)
        db.session.commit()

        return Coordinate.serialize(coordinate_record), 201
