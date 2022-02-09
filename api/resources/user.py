from api import Resource, reqparse, db
from api.schemas.user import user_schema, users_schema
from api.models.user import UserModel


class UserResource(Resource):
    def get(self, user_id=None):
        user = UserModel.query.get(user_id)
        if not user:
            return {"Error": f"User with id={user_id} not found"}, 404
        return user_schema.dump(user), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        data = parser.parse_args()
        user = UserModel(**data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201

