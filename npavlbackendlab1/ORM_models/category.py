from npavlbackendlab1.data import db


class CategoryModel(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    note = db.relationship("NoteModel", back_populates="category", lazy="dynamic")
