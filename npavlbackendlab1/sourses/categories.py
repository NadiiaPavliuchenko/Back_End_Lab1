import uuid

from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, request, abort, make_response
from npavlbackendlab1.data import CATEGORIES
from npavlbackendlab1.schema import Category_schema

blp = Blueprint("newCategory", __name__)


@blp.route("/category/<string:categoryname>")
class GetCategories(MethodView):
    def get(self, categoryname):
        cat_key = 0
        for i in range(len(CATEGORIES)):
            if categoryname == CATEGORIES[i]['name']:
                if CATEGORIES[i]['name'] != 0:
                    cat_key = CATEGORIES[i]['name']
        if cat_key != 0:
            return jsonify(cat_key)
        else:
            abort(make_response(jsonify(error='no such category'), 404))


@blp.route("/newCategory")
class NewCategory(MethodView):
    def get(self):
        return CATEGORIES

    @blp.arguments(Category_schema)
    def post(self, new_category):
        categoryname = new_category["name"]
        cat_list = list(filter(lambda newCat: newCat["name"] == categoryname, CATEGORIES))
        if len(cat_list) != 0:
            abort(make_response(jsonify(error='db contains such category'), 400))
        categooryId = uuid.uuid4().hex
        category = {"id": categooryId, "name": categoryname}
        CATEGORIES.append(category)
        return jsonify(category)
