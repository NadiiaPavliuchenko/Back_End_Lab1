from flask import jsonify

from npavlbackendlab1 import app
from flask_smorest import Api
from flask_migrate import Migrate

import os
from flask_jwt_extended import JWTManager

from npavlbackendlab1.data import db
from npavlbackendlab1.sourses.user import blp as UsersBlp
from npavlbackendlab1.sourses.categories import blp as CategoriesBlp
from npavlbackendlab1.sourses.notes import blp as NoteBlp
from npavlbackendlab1.sourses.score import blp as ScoreBlp


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "labs rest api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#JWT_SECRET_KEY = "232096237174375630521750861011649974963"
app.config["JWT_SECRET_KEY"] = "232096237174375630521750861011649974963"#os.getenv("JWT_SECRET_KEY")

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()


api.register_blueprint(UsersBlp)
api.register_blueprint(CategoriesBlp)
api.register_blueprint(NoteBlp)
api.register_blueprint(ScoreBlp)


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
   return (
       jsonify({"message": "The token has expired.", "error": "token_expired"}),
       401,
   )


@jwt.invalid_token_loader
def invalid_token_callback(error):
   return (
       jsonify(
           {"message": "Signature verification failed.", "error": "invalid_token"}
       ),
       401,
   )


@jwt.unauthorized_loader
def missing_token_callback(error):
   return (
       jsonify(
           {
               "description": "Request does not contain an access token.",
               "error": "authorization_required",
           }
       ),
       401,
   )


@app.route("/")
def default_page():
    return "Default page"


