from flask_restful import Resource
from flask import jsonify, request, make_response

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

        coordinate_record = Coordinate(tag=args["tag"], coordinates=args["coordinates"])

        db.session.add(coordinate_record)
        db.session.commit()

        return Coordinate.serialize(coordinate_record), 201

    def delete(self, id):
        record_id = Coordinate.query.filter_by(id=id)\
            .first_or_404(description='Record with id={} is not available'.format(id))
        db.session.delete(record_id)
        db.session.commit()
        return '', 204
