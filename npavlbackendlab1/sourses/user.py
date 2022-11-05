from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, abort, make_response
from sqlalchemy.exc import IntegrityError

from npavlbackendlab1.ORM_models.user import UserModel
from npavlbackendlab1.data import db
from npavlbackendlab1.schema import User_schema

blp = Blueprint("newUser", __name__)


@blp.route("/user/<string:username>")
class GetUser(MethodView):
    @blp.response(200, User_schema)
    def get(self, username):
        user = UserModel.query.filter_by(name=username).first_or_404()
        return user


@blp.route("/newUser")
class NewUser(MethodView):
    @blp.response(200, User_schema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(User_schema)
    @blp.response(200, User_schema)
    def post(self, new_user):
        user = UserModel(**new_user)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(make_response(jsonify(error='such username consists in db'), 400))
        return user
