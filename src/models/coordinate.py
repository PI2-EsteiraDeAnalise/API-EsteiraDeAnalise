from extensions import db


class Coordinate(db.Model):

    __tablename__ = "coordinate"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String, nullable=False)
    coordinates = db.Column(db.JSON, nullable=False) 

    def __init__(self, id, tag, coordinates):
        self.id = id
        self.tag = tag
        self.coordinates = coordinates

    def serialize(self):
        return {
            "id": self.id,
            "tag": self.tag,
            "coordinates": self.coordinates
        }

    def __repr__(self):
        return "<coordinate: {}>".format(self.id)
