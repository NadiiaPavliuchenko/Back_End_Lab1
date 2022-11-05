from npavlbackendlab1 import app
from flask_smorest import Api

from npavlbackendlab1.data import db
from npavlbackendlab1.sourses.user import blp as UsersBlp
from npavlbackendlab1.sourses.categories import blp as CategoryBlp
from npavlbackendlab1.sourses.notes import blp as NoteBlp
from npavlbackendlab1.sourses.score import blp as ScoreBlp


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "labs rest api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


api = Api(app)

with app.app_context():
    db.create_all()

api.register_blueprint(UsersBlp)
api.register_blueprint(CategoryBlp)
api.register_blueprint(NoteBlp)
api.register_blueprint(ScoreBlp)


@app.route("/")
def default_page():
    return "Default page"
