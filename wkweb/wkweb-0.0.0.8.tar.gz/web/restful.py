from flask.views import MethodView
from flask import jsonify

class ResourceBase(object):
    @classmethod
    def register_api(cls, app, endpoint, url, pk='id', pk_type='int'):
        url = url.rstrip('/')
        view_func = cls.as_view(endpoint)
        methods = view_func.methods
        if 'GET' in methods:
            app.add_url_rule(url, defaults={pk: None},
                             view_func=view_func, methods=['GET', ])
            app.add_url_rule('%s/<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                             methods=['GET'])
        if 'POST' in methods:
            app.add_url_rule(url, view_func=view_func, methods=['POST', ])
        if 'PUT' in methods:
            app.add_url_rule('%s/<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                             methods=['PUT'])
        if 'DELETE' in methods:
            app.add_url_rule('%s/<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                             methods=['DELETE'])
        return app

    @classmethod
    def as_view(Base, endpoint):
        def wrap_response(resp):

            return resp
        class MyView(MethodView, Base):
            if hasattr(Base, 'get'):
                def get(self, *args, **kwargs):
                    res = Base.get(self, *args, **kwargs)
                    return res
            if hasattr(Base, 'post'):
                def post(self, *args, **kwargs):
                    res = Base.post(self, *args, **kwargs)
                    return res
            if hasattr(Base, 'put'):
                def put(self, *args, **kwargs):
                    res = Base.put(self, *args, **kwargs)
                    return res
            if hasattr(Base, 'delete'):
                def delete(self, *args, **kwargs):
                    res = Base.delete(self, *args, **kwargs)
                    return res

        return MyView.as_view(endpoint)


class Resource(ResourceBase):
    Model=None
    # pk='id'
    # def get_model_pk(self):
    #     return getattr(self.Model,self.pk)
    def get(self, resource_id):
        if resource_id is None:
            resources=self.Model.all()
            resources=[res.to_dict() for res in resources]
            return jsonify(resources)
        else:
            res=self.Model.get(resource_id)
            return jsonify(res.to_dict())
    def post(self,resource_meta):
        reso=self.Model(**resource_meta)
        self.Model.add(reso)
        return True



    def delete(self, resource_id):
        # delete a single user
        pass

    def put(self, resource_id):
        # update a single user
        pass
