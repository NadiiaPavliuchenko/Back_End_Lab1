import uuid
from datetime import datetime

from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, abort, make_response
from npavlbackendlab1.data import NOTES, USERS, CATEGORIES
from npavlbackendlab1.schema import Note_schema, NoteQuery_schema

blp = Blueprint("newNote", __name__)


@blp.route("/getNote")
class GetNote(MethodView):
    @blp.arguments(NoteQuery_schema, location="query", as_kwargs=True)
    @blp.response(200, Note_schema)
    def get(self, **kwargs):
        username = kwargs.get("username")

        if not username:
            return abort(make_response(jsonify(error='username wasn`t specified'), 404))

        id_user = 0
        for i in range(len(USERS)):
            if username == USERS[i]['name']:
                if USERS[i]['name'] != 0:
                    id_user = USERS[i]['id']

        categoryname = kwargs.get("categoryname")
        if categoryname:
            id_category = 0
            for j in range(len(CATEGORIES)):
                if categoryname == CATEGORIES[j]['name']:
                    if CATEGORIES[j]['name'] != 0:
                        id_category = CATEGORIES[j]['id']

            if id_user != 0 or id_category != 0:
                us_note = list(filter(lambda user: user["id_user"] == id_user, NOTES))
                us_cat_note = list(filter(lambda cat: cat["id_category"] == id_category, us_note))
                return jsonify(us_cat_note)
            else:
                abort(make_response(jsonify(error='no such user or category'), 404))

        id_user_notes = list(filter(lambda user: user["id_user"] == id_user, NOTES))
        return jsonify(id_user_notes)


@blp.route("/newNote")
class Note(MethodView):
    @blp.response(200, Note_schema(many=True))
    def get(self):
        return NOTES

    @blp.arguments(Note_schema)
    @blp.response(200, Note_schema)
    def post(self, new_note):
        us_list = list(filter(lambda user: user["id"] == new_note["id_user"], USERS))
        cat_list = list(filter(lambda category: category["id"] == new_note["id_category"], CATEGORIES))

        if us_list == 0 or cat_list == 0:
            abort(make_response(jsonify(error='no such user or category'), 404))

        noteId = uuid.uuid4().hex
        note = {"id": noteId, "datetime": datetime.now(), **new_note}
        NOTES.append(note)
        return jsonify(note)

