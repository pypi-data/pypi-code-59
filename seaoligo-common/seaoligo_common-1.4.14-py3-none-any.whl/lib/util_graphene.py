import os
from graphene import AbstractType, Enum, Int
from flask import current_app, g, request
from werkzeug.exceptions import Unauthorized


class AuthorizationMiddleware(object):
    def resolve(self, next, root, info, **args):
        if (
            info.context.get('current_user')  # Valid login credentials provided
            or info.field_name in ['_service', 'sdl', '__typename']  # Gateway initialization
            or (os.environ.get('FLASK_ENV') == 'development'
                and ((info.field_name in ['__typename'])  # GraphQL Playground initialization
                     or request.headers.get('origin') ==
                     f"http://localhost:{os.environ.get('NODE_PORT')}"))  # GraphiQL request
            or current_app.config['TESTING']  # Test environment
        ):
            return next(root, info, **args)
        else:
            raise Unauthorized()


class Counts(AbstractType):
    total_count = Int()
    def resolve_total_count(root, info):
        return g.total_count

    filtered_count = Int()
    def resolve_filtered_count(root, info):
        return g.filtered_count


class OrganismSelect(Enum):
    HUMAN = 'human'
    MOUSE = 'mouse'
    # RAT = 'rat'


class AssemblySelect(Enum):
    hg38 = 'hg38'
    mm10 = 'mm10'
    # rn6 = 'rn6'
