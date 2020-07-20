import os

import requests
from requests import Response


def exporter(
    guid: str, file_type: str = "PDF", width: int = 2000, height: int = 2000,
) -> Response:
    """
    New Relic Dashboard exporter.
    :param guid: The New Relic dashboard GUID.
    :param file_type: The output file type. Choose either PDF or PNG.
    :param width: The width of the dashboard. Max is 2000.
    :param height: The height of the dashboard. Max is 2000.
    :return: API Response.
    """
    if not os.getenv("NEW_RELIC_PERSONAL_API_KEY"):
        raise Exception("A New Relic API key required.")

    headers = {
        "Content-Type": "application/json",
        "API-Key": os.getenv("NEW_RELIC_PERSONAL_API_KEY"),
    }

    endpoint_url = (
        "https://api.eu.newrelic.com/graphql"
        if os.getenv("NEW_RELIC_REGION") == "EU"
        else "https://api.newrelic.com/graphql"
    )

    if not guid or not guid.strip():
        raise Exception("Dashboard GUID required.")

    query = (
        """
    mutation {
        dashboardCreateSnapshotUrl(guid: "%s")
    }
    """
        % guid
    )

    req = requests.post(url=endpoint_url, json={"query": query}, headers=headers)

    if not req.ok:
        req.raise_for_status()

    resp = req.json()
    url = resp["data"]["dashboardCreateSnapshotUrl"]

    if url is None:
        raise Exception("Dashboard not found.")

    url = url.split("?", 1)[0] + "?format=%s&width=%s&height=%s" % (
        file_type,
        width,
        height,
    )

    resp = requests.get(url=url)
    return resp
