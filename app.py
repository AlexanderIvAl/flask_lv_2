from api import api, app
from config import Config
from api.resources.user import UserResource
from api.resources.quote import QuoteResource
from api.resources.token import TokenResource
from api.resources.author import AuthorResource


api.add_resource(QuoteResource,
                '/authors/<int:author_id>/quotes/<int:quote_id>',
                '/authors/<int:author_id>/quotes',
                '/quotes'
                )  # <-- requests
api.add_resource(AuthorResource,
                '/authors/<int:author_id>',
                '/authors')  # <-- requests
api.add_resource(UserResource,
                '/users/<int:user_id>', #GET
                '/users')               #POST
api.add_resource(TokenResource,'/auth/token')

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
