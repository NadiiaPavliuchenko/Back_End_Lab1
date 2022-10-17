import uuid
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