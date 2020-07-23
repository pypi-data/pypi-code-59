import os, sys, json, logging
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt

from pprint import pprint

from .cli import splash, list_menu, app_menu, input_prompt
from .io import load_config

from ..core.api import StoppingProblem
from ..core.schema import Adapter, ExperimentSchema
from ..backend import Backend


# Applications built using the core API and backend functionality


def simulate(experiment_config, backend_config):

    backend = Backend(**backend_config)
    stoppingProblem = StoppingProblem.from_config(experiment_config)

    result = stoppingProblem.run()

    experiment_config["results"] = result
    experiment_config["results"]["timestamp"] = datetime.now().isoformat()

    experiment_dict = Adapter.jsonify(experiment_config)
    backend.save(experiment_dict)
    return 0


def optimise(config, **kwargs):

    print("Stand-in for optimisation")

    return 0


def view_simulation(backend_config):

    FOLDER = backend_config["loc"]
    files = [
        f
        for f in os.listdir(FOLDER)
        if (
            os.path.isfile(os.path.join(FOLDER, f))
            and os.path.splitext(os.path.join(FOLDER, f))[-1] == ".json"
        )
    ]
    if not files:
        print("No json files in chosen directory {}".format(FOLDER))
        sys.exit(1)

    files.sort(reverse=True)
    file_options = {"file": files}

    experiment_file = list_menu(file_options)["file"]

    file_to_load = os.path.join(FOLDER, experiment_file)
    with open(file_to_load) as f:
        data = json.load(f)

    results = data["results"]

    es = ExperimentSchema()

    validated_results_data = es.load(results)

    filter_history = np.array(validated_results_data["filter_history"])
    observation_history = np.array(validated_results_data["observation_history"])
    state_history = np.array(validated_results_data["state_history"])

    post_change_belief = np.sum(
        filter_history[:, validated_results_data["post_change_states"]], 1
    )

    CHANGE_PT_COLOUR = "m"

    t = np.linspace(1, len(state_history), len(state_history))
    plt.subplot(311)
    plt.plot(t, state_history)

    plt.subplot(312)
    plt.plot(t, post_change_belief)
    axes = plt.gca()
    axes.set_ylim([0, 1])

    plt.subplot(313)
    plt.plot(t, observation_history)

    if validated_results_data["change_point"] is not None:
        change_point = validated_results_data["change_point"]
        plt.axvline(change_point, c=CHANGE_PT_COLOUR, ymin=0, ymax=1)

    FORMAT = ".png"
    SAVE_LOCATION = input_prompt(msg="Save to:", default=FOLDER)
    SAVE_FILE = os.path.splitext(experiment_file)[0] + FORMAT

    OUT_FILE = os.path.join(SAVE_LOCATION, SAVE_FILE)

    plt.savefig(OUT_FILE)

    print("Saved to {}".format(OUT_FILE))
    plt.show()


def get_config(config, **kwargs):

    cwd = os.getcwd()
    filename = os.path.join(cwd, "config.json")

    with open(filename, "w") as outfile:
        json.dump(config, outfile)

    print("Written config to {}".format(filename))


application_types = {
    "simulate": simulate,
    "optimise": optimise,
    "view": view_simulation,
    "getconf": get_config,
}


def get_app_list():
    return list(application_types.keys())


def launch(args):

    splash("Quickest")

    if args.application:
        application_str = args.application
    else:
        application_str = app_menu(application_types)

    if args.loc:
        outfolder = args.loc
    else:
        outfolder = os.getcwd()

    backend_config = {"loc": outfolder}

    if application_str == "view":
        return view_simulation(backend_config)

    if args.conf:
        print("Got config file {}".format(args.conf))
        config_dict = load_config(args.conf)

    else:
        print("No config supplied - creating one now")
        choices = list_menu(StoppingProblem.get_opts())
        config_dict = StoppingProblem.get_config(choices)

    if application_str == 'getconf':
        return get_config(config_dict)
    else:
        return application_types[application_str](config_dict, backend_config)

