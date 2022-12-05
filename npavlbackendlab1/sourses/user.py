from flask_jwt_extended import jwt_required, create_access_token
from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, abort, make_response
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError

from npavlbackendlab1.ORM_models.user import UserModel
from npavlbackendlab1.data import db
from npavlbackendlab1.schema import User_schema

blp = Blueprint("newUser", __name__)


@blp.route("/user/<string:username>")
@jwt_required()
class GetUser(MethodView):
    @blp.response(200, User_schema)
    def get(self, username):
        user = UserModel.query.filter_by(name=username).first_or_404()
        return user


@blp.route("/registerUser")
class NewUser(MethodView):
    @blp.arguments(User_schema)
    @blp.response(200, User_schema)
    def post(self, new_user):
        user = UserModel(
            name=new_user["name"],
            password=pbkdf2_sha256.hash(new_user["password"]),
        )
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(make_response(jsonify(error='such username consists in db'), 400))
        return user


@blp.route("/allUsers")
class Users(MethodView):
    @blp.response(200, User_schema(many=True))
    def get(self):
        return UserModel.query.all()