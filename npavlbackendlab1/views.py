from npavlbackendlab1 import app
from flask_smorest import Api

from npavlbackendlab1.sourses.user import blp as UsersBlp
from npavlbackendlab1.sourses.categories import blp as CategoryBlp
from npavlbackendlab1.sourses.notes import blp as NoteBlp


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "labs rest api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"

api = Api(app)

api.register_blueprint(UsersBlp)
api.register_blueprint(CategoryBlp)
api.register_blueprint(NoteBlp)


@app.route("/")
def default_page():
    return "Default page"
