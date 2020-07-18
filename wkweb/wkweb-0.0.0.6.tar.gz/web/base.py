from flask import Flask, request, send_file, session, jsonify, Blueprint,abort
import os,uuid
from . import utils as ut
from wk import join_path
class Appication(Flask):
    pass
class NestableBlueprint(Blueprint):
    def __init__(
            self,
            name,
            import_name,
            static_folder=None,
            static_url_path=None,
            template_folder=None,
            url_prefix=None,
            subdomain=None,
            url_defaults=None,
            root_path=None,
            static_map=None,
            *args, **kwargs
    ):
        super().__init__(name=name, import_name=import_name, static_folder=static_folder,
                         static_url_path=static_url_path, template_folder=template_folder, url_prefix=url_prefix,
                         subdomain=subdomain, url_defaults=url_defaults, root_path=root_path,  *args, **kwargs)
        self.blueprints=[]
        self.static_map=static_map or {}
    def register(self, app, options, first_registration=False):
        # register self
        self.add_static_map_handlers()
        Blueprint.register(self,app,options,first_registration=first_registration)
        prefix=options.get('url_prefix',None)
        if prefix:
            self.url_prefix=prefix
        # register children blueprints
        for child in self.blueprints:
            bp=child['blueprint']
            register_options=child['register_options']
            bp_prefix=register_options.pop('url_prefix',bp.url_prefix)
            print(bp_prefix,self.url_prefix,register_options)
            if bp_prefix and self.url_prefix:
                bp_prefix=self.url_prefix+bp_prefix
                print(bp_prefix,self.url_prefix)
            app.register_blueprint(bp,url_prefix=bp_prefix,**register_options)
    def register_blueprint(self, blueprint, **options):
        self.blueprints.append(dict(
            blueprint=blueprint,register_options=options
        ))
    def add_statics(self,url_folder_map:dict):
        self.static_map.update(url_folder_map)
    def add_static(self, static_url_path, static_folder):
        self.static_map[static_url_path]=static_folder
    def add_static_map_handlers(self):
        if self.static_map:
            for url_prefix,folder in self.static_map.items():
                if not url_prefix.endswith('/'):url_prefix+='/'
                @self.route(url_prefix, defaults={'req_path': ''})
                @self.route(url_prefix + '<path:req_path>')
                @ut.rename_func("static-handler-" + uuid.uuid4().hex)
                def static_handler(req_path):
                    BASE_DIR = folder
                    abs_path = os.path.join(BASE_DIR, req_path)
                    abs_path = os.path.abspath(abs_path)
                    if not os.path.exists(abs_path):
                        return abort(404)
                    if os.path.isfile(abs_path):
                        return send_file(abs_path)
                    if os.path.isdir(abs_path):
                        fns = os.listdir(abs_path)
                        urls = [join_path(self.url_prefix, url_prefix, req_path, f) for f in fns]
                        dic=dict(zip(urls,fns))
                        string=[f'<li><a href="{url}">{filename}</a></li>' for url,filename in dic.items()]
                        string=f"<ul>{''.join(string)}</ul>"
                        return string


