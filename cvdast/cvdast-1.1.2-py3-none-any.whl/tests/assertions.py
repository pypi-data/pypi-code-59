
from dictor import dictor

ANOMALY_THRESHOLD = 0

def lookup(key, dictionary):
    for k, v in dictionary.iteritems():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in lookup(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in lookup(key, d):
                    yield result



def assert_for_v1_providers(req, resp):
    assert resp.status_code == 200


def assert_for_v1_channels(req, resp):
    assert resp.status_code == 200


def assert_for_v1_feeditems_navigation_homeshortcuts(req, resp):
    assert resp.status_code == 200


def assert_for_v1_guiderowsdetail(req, resp):
    assert resp.status_code == 200


def assert_for_v1_socuvodoffers(req, resp):
    assert resp.status_code == 200


def assert_for_providers(req, resp):
    assert resp.status_code == 200


def assert_for_channels(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_search(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_navigation_homeshortcuts(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_screens_wtwmain46(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_screens_screenname(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_carousels_carouselname(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_carousels_morelikethis(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_screens_episodes(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_carousels_seasonepisodes(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_screens_linearplaybackcontextbars(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_screens_vodplaybackcontextbars(req, resp):
    assert resp.status_code == 200


def assert_for_feeditems_screens_searchcontextbars(req, resp):
    assert resp.status_code == 200


def assert_for_guiderowsdetail(req, resp):
    assert resp.status_code == 200


def assert_for_series_seriespreview_seriesid(req, resp):
    assert resp.status_code == 200


def assert_for_movies_moviepreview_movieid(req, resp):
    assert resp.status_code == 200


def assert_for_content_contentpreview_contentid(req, resp):
    assert resp.status_code == 200


def assert_for_offers_contentid(req, resp):
    assert resp.status_code == 200


def assert_for_socuvodoffers(req, resp):
    assert resp.status_code == 200


def assert_for_negative_scenarios(req, resp):
    if resp.status_code != 200:
        print("----------------------")
        print("Request: "+str(req))
        print("Response: "+str(resp))
        print("----------------------")
    assert resp.status_code != 200



def assert_for_custom_response(req, resp, keys_to_check):
    for k, v in keys_to_check.items():
        print("checking for "+str(k)+" in response: "+str(resp.json()))
        assert v == lookup(k, resp.json())