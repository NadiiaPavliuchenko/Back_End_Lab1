import uuid
from lab1 import app
from flask import jsonify, request

USERS = [
    {
        "id": uuid.uuid4().hex,
        "name": "Ann"
    },
    {
        "id": uuid.uuid4().hex,
        "name": "Andy"
    }
]

CATEGORIES = [
    {
        "id": uuid.uuid4().hex,
        "name": "clothes"
    },
    {
        "id": uuid.uuid4().hex,
        "name": "studying"
    },
    {
        "id": uuid.uuid4().hex,
        "name": "bills"
    },
    {
        "id": uuid.uuid4().hex,
        "name": "health"
    }
]


@app.route("/")
def default_page():
    return "Default page"


@app.route("/newUser", methods=['POST'])
def create_user():
    new_user = request.get_json()
    USERS.append(new_user)
    print(USERS)
    return jsonify(new_user)


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


