import click
import uvicorn

from spell.serving.server import make_api, make_app


@click.command()
@click.option("--config", required=True, type=click.File(), help="Path to the config file")
@click.option(
    "--entrypoint", type=click.Path(exists=True), help="(Deprecated) Path to the entrypoint",
)
@click.option(
    "--module-path",
    type=click.Path(exists=True),
    help="Filepath to the Python module containing predictor",
)
@click.option("--python-path", help="Python path to the module containing the predictor")
@click.option("--classname", help="Name of the predictor class")
@click.option("--host", default="0.0.0.0", help="Host to run the server on")
@click.option("--port", default=80, type=int, help="Port to run the server on")
@click.option("--debug", is_flag=True, default=False, help="Run the server in debug mode")
def start_server(config, entrypoint, module_path, python_path, classname, host, port, debug):
    """Start serving a model

    Used inside the container which runs a uvicorn server which wraps and serves the predictor
    class
    """
    # TODO(Justin): Remove entrypoint flag and make python_path and module_path required after API/CLI migration
    api = make_api(
        config,
        entrypoint=entrypoint,
        module_path=module_path,
        python_path=python_path,
        classname=classname,
    )
    uvicorn.run(make_app(api, debug=debug), http="h11", loop="asyncio", host=host, port=port)
