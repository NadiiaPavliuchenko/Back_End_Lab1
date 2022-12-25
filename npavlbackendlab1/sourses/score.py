from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, abort, make_response
from sqlalchemy.exc import IntegrityError

from npavlbackendlab1.ORM_models import UserModel, ScoreModel
from npavlbackendlab1.data import db
from npavlbackendlab1.schema import ScoreQuery_schema, Score_schema, ChangeScore_schema

blp = Blueprint("newScore", __name__)


@jwt_required()
@blp.route("/score")
class GetScore(MethodView):
    @blp.arguments(ScoreQuery_schema, location="query", as_kwargs=True)
    @blp.response(200, Score_schema(many=True))
    def get(self, **kwargs):
        username = kwargs.get("username")

        if not username:
            return abort(make_response(jsonify(error='username wasn`t specified'), 404))

        user = UserModel.query.filter_by(name=username).first_or_404()
        user_score_id = user.id
        query = ScoreModel.query.filter(ScoreModel.id_user == user_score_id)

        return query.all()


@jwt_required()
@blp.route("/addScore")
class AddScore(MethodView):
    @blp.arguments(Score_schema)
    @blp.response(200, Score_schema)
    def post(self, new_score):
        score = ScoreModel(**new_score)
        try:
            db.session.add(score)
            db.session.commit()
        except IntegrityError:
            abort(make_response(jsonify(error='incorrect input'), 400))
        return score


@jwt_required()
@blp.route("/changeScoreByUser")
class ChangeScore(MethodView):
    @blp.arguments(ChangeScore_schema, location="query", as_kwargs=True)
    @blp.response(200, Score_schema(many=True))
    def post(self, **kwargs):
        username = kwargs.get("username")

        if not username:
            return abort(make_response(jsonify(error='username wasn`t specified'), 404))

        user = UserModel.query.filter_by(name=username).first_or_404()
        user_id = user.id

        add_sum = kwargs.get("add_sum")

        if add_sum:
            userscore = ScoreModel.query.filter(ScoreModel.id_user == user_id).first_or_404()
            userscore.sum += add_sum
            db.session.commit()

        query = ScoreModel.query.filter(ScoreModel.id_user == user_id)
        return query.all()
