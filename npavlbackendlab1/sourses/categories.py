from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, abort, make_response
from sqlalchemy.exc import IntegrityError

from npavlbackendlab1.ORM_models import CategoryModel
from npavlbackendlab1.data import db
from npavlbackendlab1.schema import Category_schema

blp = Blueprint("newCategory", __name__)


@blp.route("/category/<string:categoryname>")
@jwt_required()
class GetCategories(MethodView):
    @blp.response(200, Category_schema)
    def get(self, categoryname):
        category = CategoryModel.query.filter_by(name=categoryname).first_or_404()
        return category


@blp.route("/newCategory")
@jwt_required()
class NewCategory(MethodView):
    @blp.response(200, Category_schema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(Category_schema)
    @blp.response(200, Category_schema)
    def post(self, new_category):
        category = CategoryModel(**new_category)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(make_response(jsonify(error='such category consists in db'), 400))
        return category
