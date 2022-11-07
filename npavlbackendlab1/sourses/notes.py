from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, abort, make_response
from sqlalchemy.exc import IntegrityError

from npavlbackendlab1.ORM_models import NoteModel, UserModel, CategoryModel, ScoreModel
from npavlbackendlab1.data import db
from npavlbackendlab1.schema import Note_schema, NoteQuery_schema

blp = Blueprint("newNote", __name__)


@blp.route("/getNote")
class GetNote(MethodView):
    @blp.arguments(NoteQuery_schema, location="query", as_kwargs=True)
    @blp.response(200, Note_schema(many=True))
    def get(self, **kwargs):
        username = kwargs.get("username")

        if not username:
            return abort(make_response(jsonify(error='username wasn`t specified'), 404))

        user = UserModel.query.filter_by(name=username).first_or_404()
        user_id = user.id
        query = NoteModel.query.filter(NoteModel.id_user == user_id)

        categoryname = kwargs.get("categoryname")

        if categoryname:
            category = CategoryModel.query.filter_by(name=categoryname).first_or_404()
            category_id = category.id
            query = query.filter(NoteModel.id_category == category_id)

        return query.all()


@blp.route("/newNote")
class Note(MethodView):
    @blp.response(200, Note_schema(many=True))
    def get(self):
        return NoteModel.query.all()

    @blp.arguments(Note_schema)
    @blp.response(200, Note_schema)
    def post(self, new_note):
        note = NoteModel(**new_note)
        new_sum = note.sum
        user_id = note.id_user

        userscore = ScoreModel.query.filter(ScoreModel.id_user == user_id).first_or_404()

        try:
            db.session.add(note)
            userscore.sum -= new_sum
            if userscore.sum < 0:
                abort(make_response(jsonify(error='you don`t have enough money'), 400))
            db.session.commit()
        except IntegrityError:
            abort(make_response(jsonify(error='incorrect input'), 400))
        return note

