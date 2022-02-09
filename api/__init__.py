from config import Config
from flask import Flask, request, g
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth


class UnicodeApi(Api):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app.config['RESTFUL_JSON'] = {
            'ensure_ascii': False,
        }


app = Flask(__name__)
app.config.from_object(Config)
api = UnicodeApi(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    from api.models.user import UserModel
    user = UserModel.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True
