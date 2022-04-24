from flask_restful import Resource

from extensions import db
from models.coordinate import Coordinate as Coord


class Coordinate(Resource):
    def delete(self, record_id):
        record = Coord.query.filter_by(id=record_id).first_or_404(
            description=f"Record with id={record_id} is not available"
        )
        db.session.delete(record)
        db.session.commit()
        return "", 204
