# temporary file for testing search abstractions
# TODO: Delete this file!!

from elasticsearch import Elasticsearch, ConnectionError

es = Elasticsearch([{'host': "localhost", 'port': 9200}])


def run_query(index_name, search_query, body_field, secondary_fields, max_documents=5, highlight_span=100, relsnip=True, num_fragments=5):

    tags = {"pre_tags": [""], "post_tags": [""]}
    highlight_params = {
        "fragment_size": highlight_span,
        "fields": {
            "casebody": tags,
            "author": tags
        },
        "number_of_fragments": num_fragments,
        # "order": "score"
    }

    search_query = {
        "query": {
            "multi_match": {
                "query":    search_query,
                "fields": [body_field] + secondary_fields
            }
        },
        "size": max_documents
    }

    status = True
    results = []

    if (relsnip):
        search_query["_source"] = {"includes": [""]}
        search_query["highlight"] = highlight_params
    else:
        search_query["_source"] = {"includes": [body_field]}

    try:
        query_result = es.search(index="supremecourt", body=search_query)
        # RelSnip: for each document, we concatenate all
        # fragments in each document and return as the document.
        print(query_result["hits"]["hits"])
        highlights = [" *** ".join(hit["highlight"][body_field])
                      for hit in query_result["hits"]["hits"] if "highlight" in hit]
        docs = [((hit["_source"][body_field][:-1]))
                for hit in query_result["hits"]["hits"] if hit["_source"]]
        took = query_result["took"]
        results = {"took": took,  "highlight": highlights, "docs": docs}

    except (ConnectionRefusedError, Exception) as e:
        status = False
        results = str(e)

    results["status"] = status
    return results


search_query = "what is the fourth ammendment"
max_documents = 1
highlight_span = 50
body_field = "casebody"
secondary_fields = ["author"]
num_fragments = 2

results = run_query("supremecourt", search_query, body_field, secondary_fields,
                    max_documents=5, highlight_span=highlight_span, relsnip=True, num_fragments=num_fragments)
print(results)
