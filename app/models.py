from app import db


class Score(db.Model):
    __tablename__ = 'scores'

    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer)
    time = db.Column(db.Integer)
    name = db.Column(db.String())

    def __init__(self, points, time, name):
        self.points = points
        self.time = time
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

