from api.models.user import UserModel
from api import Resource, reqparse, db
from api.schemas.user import user_schema, users_schema


class UserResource(Resource):
    def get(self, user_id=None):
        if user_id is None:
            users = UserModel.query.all()
            return [user_schema.dump(user) for user in users]
                
        user = UserModel.query.get(user_id)
        if not user:
            return {"Error": f"User with id={user_id} not found"}, 404
        return user_schema.dump(user), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        parser.add_argument("role")
        data = parser.parse_args()
        user = UserModel(**data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("username")
        parser.add_argument("password")
        parser.add_argument("role")
        user_data = parser.parse_args()
        user = UserModel.query.get(user_id)
        if user is None:
            return f"User with id {user_id} not found", 404
        if user_data["username"]:
            user.username = user_data["username"]
        if user_data["role"]:
            user.role = user_data["role"]
        if user_data["password"]:
            user.hash_password(user_data["password"])
        db.session.commit()
        return user_schema.dump(user), 200

    def delete(self, user_id):
        user = UserModel.query.get(user_id)
        if user is None:
            return f"User with id {user_id} not found", 404
        db.session.delete(user)
        db.session.commit()
        return user_schema.dump(user), 200