from extensions import db


class Board(db.Model):

    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date(), nullable=False, default=db.func.current_date())
    sucess = db.Column(db.Boolean, nullable=False)

    def __init__(self, sucess):
        self.sucess = sucess

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date.__str__(),
            "sucess": self.sucess,
        }

    def __repr__(self):
        return "<board: {}>".format(self.id)
