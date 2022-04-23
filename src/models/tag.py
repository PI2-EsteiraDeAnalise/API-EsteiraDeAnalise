from extensions import db


class Tag(db.Model):

    __tablename__ = "tags"

    name = db.Column(db.String(50), primary_key=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            "name": self.name,
        }

    def __repr__(self):
        return "<tag: {}>".format(self.name)
