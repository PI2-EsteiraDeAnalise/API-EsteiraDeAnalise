from extensions import db


class Coordinate(db.Model):

    __tablename__ = "coordinate"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String, nullable=False)
    x1 = db.Column(db.Float, nullable=False)
    y1 = db.Column(db.Float, nullable=False)
    x2 = db.Column(db.Float, nullable=False)
    y2 = db.Column(db.Float, nullable=False)

    def __init__(self, id, tag, x1, y1, x2, y2):
        self.id = id
        self.tag = tag
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def serialize(self):
        return {
            "id": self.id,
            "tag": self.tag,
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2,
        }

    def __repr__(self):
        return "<coordinate: {}>".format(self.id)
