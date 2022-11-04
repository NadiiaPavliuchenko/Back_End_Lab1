import uuid

from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, request, abort, make_response
from npavlbackendlab1.data import USERS
from npavlbackendlab1.schema import User_schema

blp = Blueprint("newUser", __name__)


@blp.route("/user/<string:username>")
class GetUser(MethodView):
    def get(self, username):
        user_key = 0
        for i in range(len(USERS)):
            if username == USERS[i]['name']:
                if USERS[i]['name'] != 0:
                    user_key = USERS[i]['name']
        if user_key != 0:
            return jsonify(user_key)
        else:
            abort(make_response(jsonify(error='no such category'), 404))


@blp.route("/newUser")
class NewUser(MethodView):
    def get(self):
        return USERS

    @blp.arguments(User_schema)
    def post(self, new_user):
        username = new_user["name"]
        us_list = list(filter(lambda nUser: nUser["name"] == username, USERS))
        if len(us_list) != 0:
            abort(make_response(jsonify(error='db contains such name'), 400))
        userId = uuid.uuid4().hex
        user = {"id": userId, "name": username}
        USERS.append(user)
        return jsonify(user)
