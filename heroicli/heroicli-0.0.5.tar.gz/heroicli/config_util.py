import yaml


def load_config(config):
    with open(config) as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def get_heroic_url(config):
    return load_config(config)["heroicli"]["heroic"]["url"]
