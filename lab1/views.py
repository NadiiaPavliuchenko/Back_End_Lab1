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

NOTES = [
    {
        "id": uuid.uuid4().hex,
        "id_user": USERS[0]["id"],
        "id_category": CATEGORIES[3]["id"],
        "datetime": "2022.10.10 14:20",
        "sum": "400"
    },
    {
        "id": uuid.uuid4().hex,
        "id_user": USERS[0]["id"],
        "id_category": CATEGORIES[0]["id"],
        "datetime": "2022.10.10 15:55",
        "sum": "100"
    },
    {
        "id": uuid.uuid4().hex,
        "id_user": USERS[1]["id"],
        "id_category": CATEGORIES[2]["id"],
        "datetime": "2022.11.10 12:00",
        "sum": "800"
    },
    {
        "id": uuid.uuid4().hex,
        "id_user": USERS[1]["id"],
        "id_category": CATEGORIES[1]["id"],
        "datetime": "2022.11.10 12:20",
        "sum": "300"
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


@app.route("/newCategory", methods=['POST'])
def create_category():
    new_category = request.get_json()
    CATEGORIES.append(new_category)
    print(CATEGORIES)
    return jsonify(new_category)


@app.route("/newNote", methods=['POST'])
def create_note():
    new_note = request.get_json()
    NOTES.append(new_note)
    print(NOTES)
    return jsonify(new_note)
