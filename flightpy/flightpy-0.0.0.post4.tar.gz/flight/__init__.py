from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from .exceptions import ConfigException
import json

class Flight:

    def __init__(self):
        # NOTE: can be anything you like, but dev is reserved for dev.
        self.mode = "dev"
        self.routes = []
        # self.type = "app" # can be app, or api

    # NOTE: register a get request handler
    def get(self, route, fn):
        self.routes.append(Rule(route, methods=['GET'], endpoint=fn))

    # NOTE: register a put request handler
    def put(self, route, fn):
        self.routes.append(Rule(route, methods=['PUT'], endpoint=fn))

    # NOTE: register a post request handler
    def post(self, route, fn):
        self.routes.append(Rule(route, methods=['POST'], endpoint=fn))
    
    # NOTE: register a delete request handler
    def delete(self, route, fn):
        self.routes.append(Rule(route, methods=['DELETE'], endpoint=fn))
    # TODO: consider adding other http methods (PATCH)

    # NOTE: register other middleware functions
    def use(self):
        pass

class Run:
    def __init__(self, app):
        self.app = app
        self.rules = Map(self.app.routes)

    def __call__(self, env, res):
        self.env = env
        self.req = Request(env)
        self.res = Response()
        adapter = self.rules.bind_to_environ(self.req.environ)
        endpoint, values = adapter.match()
        results = endpoint(self.req, self.res, **values)
        mt = "text/html"
        try:
            json.loads(results)
            mt = "application/json"
        except Exception as e:
            pass
        
        self.res.mimetype = mt
        self.res.data = results
        return self.res(self.env, res)