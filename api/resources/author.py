from api.models.author import AuthorModel
from api import Resource, reqparse, db, auth
from api.schemas.author import author_schema, authors_schema


class AuthorResource(Resource):
    @auth.login_required
    def get(self, author_id=None):
        if author_id is None:
            authors = AuthorModel.query.all()
            # authors_list = [author.to_dict() for author in authors]
            return authors_schema.dump(authors), 200

        author = AuthorModel.query.get(author_id)
        if not author:
            return f"Author id={author_id} not found", 404
        # return author.to_dict(), 200
        return author_schema.dump(author), 200

    @auth.login_required(role='admin')
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        parser.add_argument("surname", required=True)
        author_data = parser.parse_args()

        author = AuthorModel(author_data["name"], author_data["surname"])
        db.session.add(author)
        db.session.commit()
        return author_schema.dump(author), 201

    @auth.login_required
    def put(self, author_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        parser.add_argument("surname", required=True)
        author_data = parser.parse_args()

        author = AuthorModel.query.get(author_id)
        if author is None:
            author = AuthorModel(author_data["name"], author_data["surname"])
            db.session.add(author)
            db.session.commit()
            return author_schema.dump(author), 201
        author.name = author_data["name"]
        author.surname = author_data["surname"]
        db.session.commit()
        return author_schema.dump(author), 200

    @auth.login_required
    def delete(self, author_id):
        author = AuthorModel.query.get(author_id)
        if author is None:
            return f"Author with id {author_id} not found", 404
        db.session.delete(author)
        db.session.commit()
        return author_schema.dump(author), 200