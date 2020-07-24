from . import heroic
import json
import click


def inspect_tag(config, tag, limit, values, j):
    """get values for a specific tag"""
    query_path = "/metadata/tag-value-suggest"
    query_type = "post"
    query_data = json.dumps({"key": tag, "limit": limit})
    query_result = heroic.heroic_query(query_path, query_type, query_data, config)
    if query_result["errors"] == []:
        if query_result["limited"] is not False:
            click.echo("Results limited, increase `limit` to see full set")
        if not values and not j:
            click.echo("Tag: {}".format(tag))
            click.echo("Values: {}".format(len(query_result["values"])))
        elif not j:
            click.echo("Tag: {}".format(tag))
            click.echo("Values:")
            for v in query_result["values"]:
                click.echo(v)
        else:
            click.echo(json.dumps(query_result["values"]))
    else:
        click.echo(query_result["errors"])


def _key_inspect(config, limit):
    query_path = "/metadata/key-suggest"
    query_type = "post"
    query_data = json.dumps({"limit": limit})
    query_result = heroic.heroic_query(query_path, query_type, query_data, config)
    keys = []
    for k in query_result["suggestions"]:
        keys.append(k["key"])
    return keys


def key_inspect(config, limit, v, j):
    keys = _key_inspect(config, limit)
    print("Found {} $keys".format(len(keys)))
    if v and not j:
        for k in keys:
            click.echo(k)
    elif j:
        click.echo(json.dumps(keys))


def high_cardinality(config, limit, threshold):
    """ find high cardinality tags """
    keys = _key_inspect(config, limit)
    print("Found {} $keys to use to break up search...".format(len(keys)))
    query_path = "/metadata/tagkey-count"
    query_type = "post"
    hc_tags = {}
    for k in keys:
        print("Searching for high cardinality tags in the {} $key".format(k))
        query_data = json.dumps({"limit": limit, "filter": ["key", k]})
        query_result = heroic.heroic_query(query_path, query_type, query_data, config)
        if query_result["errors"] != []:
            click.echo(query_result["errors"])
        if query_result["limited"] is not False:
            click.echo("Results limited, increase `limit` to see full set")
        for s in query_result["suggestions"]:
            if s["count"] >= threshold:
                hc_tags[k] = {s["key"]: s["count"]}
                # hc_tags[s['key']] = s['count']

    for k, v in hc_tags.items():
        print("In $key = {}:".format(k))
        for k2, v2 in v.items():
            print("{} - {}".format(k2, v2))
        print("")
