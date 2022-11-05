from npavlbackendlab1.data import db


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    record = db.relationship("NoteModel", back_populates="user", lazy="dynamic")
