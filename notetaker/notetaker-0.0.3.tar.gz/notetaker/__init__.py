
def _jupyter_server_extension_paths():
    """
    Set up the server extension for collecting metrics
    """
    return [{"module": "notetaker"}]


def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "notetaker",
        "src": "static",
        "require": "notetaker/main"
    }]

def load_jupyter_server_extension(nbapp):
    """
    Called during notebook start
    """
    nbapp.log.info("notetaker enabled!")