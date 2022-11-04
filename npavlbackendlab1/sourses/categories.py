import uuid

from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, request, abort, make_response
from npavlbackendlab1.data import CATEGORIES

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

    def post(self):
        new_category = request.get_json()
        categoryname = new_category["name"]
        cat_list = list(filter(lambda newCat: newCat["name"] == categoryname, CATEGORIES))
        if "name" not in new_category:
            abort(make_response(jsonify(error='name wasn`t given'), 400))
        if len(cat_list) != 0:
            abort(make_response(jsonify(error='db contains such category'), 400))
        categooryId = uuid.uuid4().hex
        category = {"id": categooryId, "name": categoryname}
        CATEGORIES.append(category)
        return jsonify(category)
