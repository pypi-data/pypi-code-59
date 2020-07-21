from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wrappers import Response
from munch import munchify

# NOTE: APPHandler is designed to return a HTML response.
# NOTE: SimpleTemplate is used as the core template engine.
class APPHandler:
    
    def __init__(self, run):        
        self.run = run
        self.exe()
    
    def exe(self):
        adapter = self.run.rules.bind_to_environ(self.run.env)
        res = Response()
        res.content_type = 'text/html'
        try:
            endpoint, values = adapter.match()
            self.run.req.params = munchify(values)
            return Response(endpoint())
        except HTTPException as e:
            return Response(str(e.get_body()), e.code)