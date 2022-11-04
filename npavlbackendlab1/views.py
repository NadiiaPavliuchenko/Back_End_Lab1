from npavlbackendlab1 import app
from flask import jsonify, request
from flask_smorest import Api
from functools import wraps
from npavlbackendlab1 import data

from npavlbackendlab1.sourses.user import blp as UsersBlp

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "labs rest api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"

api = Api(app)

api.register_blueprint(UsersBlp)


@app.route("/")
def default_page():
    return "Default page"


"""@app.route("/categories")
def get_categories():
    return jsonify({"categories": data.CATEGORIES})


@app.route("/newCategory", methods=['POST'])
def create_category():
    new_category = request.get_json()
    data.CATEGORIES.append(new_category)
    print(data.CATEGORIES)
    return jsonify(new_category)


@app.route("/newNote", methods=['POST'])
def create_note():
    new_note = request.get_json()
    data.NOTES.append(new_note)
    print(data.NOTES)
    return jsonify(new_note)


def check_username(func):
    @wraps(func)
    def username_function(username):
        us_list = list(filter(lambda user: user["name"] == username, data.USERS))
        if len(us_list) != 0:
            id_user = us_list[0]["id"]
            return func(id_user)
        else:
            return f"no such username"
    return username_function


@app.route("/getNoteByUser/<username>")
@check_username
def get_note_byUser(id_user):
    us_note = list(filter(lambda user: user["id_user"] == id_user, data.NOTES))
    return jsonify(us_note)


def check_category(func):
    @wraps(func)
    def category_function(username, categoryName):
        us_list = list(filter(lambda user: user["name"] == username, data.USERS))
        cat_list = list(filter(lambda category: category["name"] == categoryName, data.CATEGORIES))
        if len(us_list) != 0 and len(cat_list) != 0:
            id_user = us_list[0]["id"]
            id_category = cat_list[0]["id"]
            return func(id_user, id_category)
        else:
            return f"no such user or category"
    return category_function


@app.route("/getNote/<username>/<categoryName>")
@check_category
def get_Note(id_user, id_category):
    us_note = list(filter(lambda user: user["id_user"] == id_user, data.NOTES))
    us_cat_note = list(filter(lambda cat: cat["id_category"] == id_category, us_note))
    return jsonify(us_cat_note)"""
