from . import config_util
import requests
import json

HEADERS = {"Content-type": "application/json"}


def heroic_query(query_path, query_type, query_data, config):
    url = config_util.get_heroic_url(config) + query_path
    if query_type == "post":
        r = requests.post(url, data=query_data, headers=HEADERS)
        results = json.loads(r.text)
    return results
