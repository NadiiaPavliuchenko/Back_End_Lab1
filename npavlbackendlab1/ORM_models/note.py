from sqlalchemy import func
from npavlbackendlab1.data import db


class NoteModel(db.Model):
    __tablename__ = "note"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id"), unique=False, nullable=False)
    id_category = db.Column(db.Integer, db.ForeignKey("category.id"), unique=False, nullable=False)
    datetime = db.Column(db.TIMESTAMP, server_default=func.now())
    sum = db.Column(db.Float(precision=2), unique=False, nullable=False)

    user = db.relationship("UserModel", back_populates="note")
    category = db.relationship("CategoryModel", back_populates="note")
