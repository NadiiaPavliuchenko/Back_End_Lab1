from npavlbackendlab1.data import db


class ScoreModel(db.Model):
    __tablename__ = "score"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id"), unique=False, nullable=False)
    sum = db.Column(db.Float(precision=2), unique=False, nullable=False)

    user = db.relationship("UserModel", back_populates="score")
