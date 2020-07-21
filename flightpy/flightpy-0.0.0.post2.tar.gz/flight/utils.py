from werkzeug.serving import run_simple

def dev_server(app, host = "127.0.0.1", port = 3000, debug = True):
    run_simple(host, port, app, use_debugger=debug, use_reloader=debug)