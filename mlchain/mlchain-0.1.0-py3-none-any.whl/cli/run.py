import click
import os
from mlchain.base import ServeModel
from mlchain.server import MLServer
import importlib
import sys
from mlchain import logger
import GPUtil

def select_gpu():
    try:
        gpus = GPUtil.getFirstAvailable()
    except:
        gpus = []
    if len(gpus) == 0:
        gpus = [0]
    while True:
        for gpu in gpus:
            yield str(gpu)


def prepare_import(path):
    """Given a filename this will try to calculate the python path, add it
    to the search path and return the actual module name that is expected.
    """
    path = os.path.realpath(path)

    fname, ext = os.path.splitext(path)
    if ext == ".py":
        path = fname

    if os.path.basename(path) == "__init__":
        path = os.path.dirname(path)

    module_name = []

    # move up until outside package structure (no __init__.py)
    while True:
        path, name = os.path.split(path)
        module_name.append(name)

        if not os.path.exists(os.path.join(path, "__init__.py")):
            break

    if sys.path[0] != path:
        sys.path.insert(0, path)

    return ".".join(module_name[::-1])


op_config = click.option("--config", "-c", default=None, help="file json or yaml")
op_name = click.option("--name", "-n", default=None, help="name service")
op_host = click.option("--host", "-h", default=None, help="The interface to bind to.")
op_port = click.option("--port", "-p", default=None, help="The port to bind to.")
op_bind = click.option("--bind", "-b", required=False, multiple=True)
op_wrapper = click.option('--wrapper', 'wrapper', flag_value=None,
                          default=True)
op_gunicorn = click.option('--gunicorn', 'wrapper', flag_value='gunicorn')
op_hypercorn = click.option('--hypercorn', 'wrapper', flag_value='hypercorn')
op_rabbit = click.option('--rabbit', 'queue', flag_value='rabbit')
op_flask = click.option('--flask', 'server', flag_value='flask')
op_quart = click.option('--quart', 'server', flag_value='quart')
op_trace = click.option('--trace', '-t', default=None, type=bool)
op_log = click.option('--log', '-l', default=None, type=bool)
op_grpc = click.option('--grpc', 'server', flag_value='grpc')
op_worker = click.option('--workers','-w', 'workers', default=None, type=int)
op_mode = click.option('--mode','-m', 'mode', default=None, type=str)
op_dump = click.option('--dump_request','-d', 'dump_request', default=None, type=str)

@click.command("run", short_help="Run a development server.")
@click.argument('entry_file', nargs=1, required=False, default=None)
@op_host
@op_port
@op_bind
@op_gunicorn
@op_hypercorn
@op_flask
@op_quart
@op_grpc
@op_rabbit
@op_worker
@op_trace
@op_log
@op_config
@op_name
@op_mode
@op_dump
@click.argument('kws', nargs=-1)
def run_command(entry_file, host, port, bind, wrapper, server, queue, workers, trace, log, config, name,mode,dump_request, kws):
    from mlchain import config as mlconfig
    default_config = False
    if config is None:
        default_config = True
        config = 'mlconfig.yaml'
    if os.path.isfile(config):
        if config.endswith('.json'):
            config = mlconfig.load_json(config)
        elif config.endswith('.yaml') or config.endswith('.yml'):
            config = mlconfig.load_yaml(config)
        else:
            raise AssertionError("Not support file config {0}".format(config))
    else:
        if not default_config:
            raise FileNotFoundError("Not found file {0}".format(config))
        config = {}
    if 'mode' in config and 'env' in config['mode']:
        if mode in config['mode']['env']:
            config['mode']['default'] = mode
    mlconfig.load_config(config)
    entry_file = mlconfig.get_value(entry_file, config, 'entry_file', 'server.py')
    host = mlconfig.get_value(host, config, 'host', 'localhost')
    port = mlconfig.get_value(port, config, 'port', 5000)
    server = mlconfig.get_value(server, config, 'server', 'flask')
    if len(bind) == 0:
        bind = None
    bind = mlconfig.get_value(bind, config, 'bind', [])
    wrapper = mlconfig.get_value(wrapper, config, 'wrapper', None)
    queue = mlconfig.get_value(queue, config, 'queue', None)
    trace = mlconfig.get_value(trace, config, 'trace', False)
    log = mlconfig.get_value(log, config, 'log', False)
    workers = mlconfig.get_value(workers, config, 'workers', None)
    name = mlconfig.get_value(name, config, 'name', None)
    monitor_sampling_rate = mlconfig.get_value(None, config, 'monitor_sampling_rate', 0)
    cors = mlconfig.get_value(None, config, 'cors', False)
    version = mlconfig.get_value(None, config, 'version', '0.0')
    version = str(version)
    dump_request = mlconfig.get_value(dump_request,config,'dump_request',None)
    api_keys = os.getenv('API_KEYS',None)
    if api_keys is not None:
        api_keys = api_keys.split(';')
    api_keys = mlconfig.get_value(api_keys,config,'api_keys',None)
    import logging
    logging.root = logging.getLogger(name)
    logger.debug(dict(
        entry_file=entry_file,
        host=host,
        port=port,
        bind=bind,
        wrapper=wrapper,
        server=server,
        queue=queue,
        workers=workers,
        log=log,
        name=name,
        trace=trace,
        mode=mode,
        dump_request = dump_request,
        kws=kws
    ))
    bind = list(bind)

    if server == 'grpc':
        from mlchain.server.grpc_server import GrpcServer
        app = get_model(entry_file, serve_model=True)
        app = GrpcServer(app, name=name)
        app.run(host, port)
    elif wrapper == 'gunicorn':
        from gunicorn.app.base import BaseApplication
        gpus = select_gpu()
        class GunicornWrapper(BaseApplication):
            def __init__(self, server_, **kwargs):
                assert server_.lower() in ['quart', 'flask']
                self.server = server_.lower()
                self.options = kwargs
                super(GunicornWrapper, self).__init__()

            def load_config(self):
                config = {key: value for key, value in self.options.items()
                          if key in self.cfg.settings and value is not None}
                for key, value in config.items():
                    self.cfg.set(key.lower(), value)

            def load(self):
                os.environ['CUDA_VISIBLE_DEVICES'] = str(next(gpus))
                app = get_model(entry_file, serve_model=True)
                if isinstance(app, ServeModel):
                    if self.server == 'flask':
                        from mlchain.server.flask_server import FlaskServer
                        app = FlaskServer(app, name=name,dump_request=dump_request,version=version,api_keys=api_keys)
                        app.register_swagger(host, port)
                        if cors:
                            from flask_cors import CORS
                            CORS(app.app)
                        return app.app
                    elif self.server == 'quart':
                        from mlchain.server.quart_server import QuartServer
                        app = QuartServer(app, name=name,dump_request=dump_request,version=version,api_keys=api_keys)
                        app.register_swagger(host, port)
                        if cors:
                            from quart_cors import cors as CORS
                            CORS(app.app)
                        return app.app
                return None

        if host is not None and port is not None:
            bind.append('{0}:{1}'.format(host, port))
        bind = list(set(bind))
        gunicorn_config = config.get('gunicorn', {})
        gunicorn_env = ['worker_class', 'threads', 'workers']
        if workers is not None:
            gunicorn_config['workers'] = workers
        def get_env(_k):
            return 'GUNICORN_' + _k.upper()

        for k in gunicorn_env:
            if get_env(k) in os.environ:
                gunicorn_config[k] = os.environ[get_env(k)]
        GunicornWrapper(server, bind=bind, **gunicorn_config).run()
    elif wrapper == 'hypercorn' and server == 'quart':
        from mlchain.server.quart_server import QuartServer
        app = get_model(entry_file, serve_model=True)
        app = QuartServer(app, name=name,version=version,dump_request=dump_request,api_keys=api_keys)
        app.run(host, port, bind=bind, cors=cors, gunicorn=False, hypercorn=True, **config.get('hypercorn', {}))

    app = get_model(entry_file)
    if isinstance(app, MLServer):
        if app.__class__.__name__ == 'FlaskServer':
            app.run(host, port, cors=cors, gunicorn=False)
        elif app.__class__.__name__ == 'QuartServer':
            app.run(host, port, cors=cors, gunicorn=False, hypercorn=False)
        elif app.__class__.__name__ == 'GrpcServer':
            app.run(host, port)
    elif isinstance(app, ServeModel):
        if server not in ['quart', 'grpc']:
            server = 'flask'
        if server == 'flask':
            from mlchain.server.flask_server import FlaskServer
            app = FlaskServer(app, name=name,dump_request=dump_request,version=version,api_keys=api_keys)
            app.run(host, port, cors=cors, gunicorn=False)
        elif server == 'quart':
            from mlchain.server.quart_server import QuartServer
            app = QuartServer(app, name=name,dump_request=dump_request,version=version,api_keys=api_keys)
            app.run(host, port, cors=cors, gunicorn=False, hypercorn=False)

        elif server == 'grpc':
            from mlchain.server.grpc_server import GrpcServer
            app = GrpcServer(app, name=name)
            app.run(host, port)


def get_model(module, serve_model=False):
    import_name = prepare_import(module)

    module = importlib.import_module(import_name)
    serve_models = [v for v in module.__dict__.values() if isinstance(v, ServeModel)]
    if len(serve_models) > 0 and serve_model:
        serve_model = serve_models[0]
        return serve_model
    apps = [v for v in module.__dict__.values() if isinstance(v, MLServer)]
    if len(apps) > 0:
        return apps[0]
    if len(serve_models) > 0:
        return serve_models[0]

    # Could not find model 
    logger.debug("Could not find ServeModel")
    serve_models = [v for v in module.__dict__.values() if not isinstance(v, type)]
    if len(serve_models) > 0 and serve_model:
        serve_model = ServeModel(serve_models[-1])
        return serve_model

    logger.error("Could not find any instance to serve")
    return None
