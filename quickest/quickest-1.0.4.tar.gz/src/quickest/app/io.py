import argparse, logging, json


def get_parser(application_options=None, backend_options=None):

    parser = argparse.ArgumentParser(
        description="Quickest Change Application entry point"
    )
    parser.add_argument(
        "application",
        type=str,
        nargs="?",
        choices=application_options,
        help="Experiment to run",
    )

    for key in backend_options:
        opts = backend_options[key]
        for opt in opts:
            parser.add_argument("--" + opt['kwarg'], help=opt['description'])

    parser.add_argument("--conf", type=str, help="Absolute path to config file")

    return parser


def get_logger(LOGFILE):

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d %(name)-16s %(levelname)-8s %(message)s",
        datefmt="%d-%m-%y %H:%M:%S",
        filename=LOGFILE,
        filemode="w",
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
    logger = logging.getLogger("quickest.app")
    return logger


def load_config(CONFIGFILE):
    with open(CONFIGFILE) as f:
        config = json.load(f)
    # TODO VALIDATION

    return config

