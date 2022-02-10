from typing_extensions import Required
from api import Resource, reqparse, db, auth
from api.models.author import AuthorModel
from api.models.quote import QuoteModel
from api.schemas.quote import quote_schema, quotes_schema


class QuoteResource(Resource):
    @auth.login_required
    def get(self, author_id=None, quote_id=None):
        """
        Обрабатываем GET запросы
        :param id: id цитаты
        :return: http-response("текст ответа", статус)
        """
        # List quotes
        if author_id is None and quote_id is None:
            quotes = QuoteModel.query.all()
            return [quote_schema.dump(quote) for quote in quotes]

        # All quotes by author id
        author = AuthorModel.query.get(author_id)
        if quote_id is None:
            quotes = author.quotes.all()
            return [quote_schema.dump(quote) for quote in quotes], 200

        # Quote by id
        quote = QuoteModel.query.get(quote_id)
        if quote:
            return quote_schema.dump(quote), 200
        return {"Error": "Quote not found"}, 404


    @auth.login_required
    def post(self, author_id):
        parser = reqparse.RequestParser()
        parser.add_argument("text", required=True)
        quote_data = parser.parse_args()
        author = AuthorModel.query.get(author_id)
        if author:
            quote = QuoteModel(author, quote_data["text"])
            db.session.add(quote)
            db.session.commit()
            return quote_schema.dump(quote), 201
        return {"Error": f"Author id={author_id} not found"}, 404


    @auth.login_required
    def put(self, author_id, quote_id):
        parser = reqparse.RequestParser()
        # parser.add_argument("author")
        parser.add_argument("text", required=True)
        new_data = parser.parse_args()
        quote = QuoteModel.query.get(quote_id)
        author = AuthorModel.query.get(author_id)
        if quote is None:
            quote = QuoteModel(author, new_data["text"])
            db.session.add(quote)
            db.session.commit()
            return quote_schema.dump(quote), 201
        # quote.author.name = new_data["author"]
        quote.text = new_data["text"]
        db.session.commit()
        return quote_schema.dump(quote), 200


    @auth.login_required
    def delete(self, author_id, quote_id):
        quote = QuoteModel.query.get(quote_id)
        author = AuthorModel.query.get(author_id)
        if quote is None:
            return f"Quote with id {quote_id} not found", 404
        db.session.delete(quote)
        db.session.commit()
        return quote_schema.dump(quote), 200
