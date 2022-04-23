from extensions import db


class Metric(db.Model):

    __tablename__ = "metrics"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    metric = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, metric, description):
        self.metric = metric
        self.description = description

    def serialize(self):
        return {
            "id": self.id,
            "metric": self.metric,
            "description": self.description,
        }

    def __repr__(self):
        return "<metric: {}>".format(self.metric)
