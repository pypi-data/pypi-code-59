"""
Search the ANTARES database for objects of interest.
"""
import json
from typing import Dict, Iterator, Optional
from urllib.parse import urljoin

import astropy.coordinates
import astropy.units

from ._api.api import get_resource, list_resource
from ._api.models import Locus, LocusSchema, LocusListingSchema
from .config import config


def search(query: Dict) -> Iterator[Locus]:
    """
    Searches the ANTARES database for loci that meet certain criteria.

    Parameters
    ----------
    query

    Returns
    -------

    """
    return list_resource(
        urljoin(config["ANTARES_API_BASE_URL"], "loci"),
        LocusListingSchema,
        params={
            "page": {"limit": -1,},
            "fields[locus_listing]": "locus",
            "elasticsearch_query[locus_listing]": json.dumps(query),
        },
    )


def cone_search(
    center: astropy.coordinates.SkyCoord, radius: astropy.coordinates.Angle
) -> Iterator[Locus]:
    return search(
        {
            "query": {
                "bool": {
                    "filter": {
                        "sky_distance": {
                            "distance": f"{radius.to_string(unit=astropy.units.deg, decimal=True)} degree",
                            "htm16": {"center": center.to_string(),},
                        },
                    },
                },
            },
        }
    )


def get_by_id(locus_id) -> Optional[Locus]:
    return get_resource(
        urljoin(config["ANTARES_API_BASE_URL"], "loci/{}".format(locus_id)),
        LocusSchema,
    )


def get_by_ztf_object_id(ztf_object_id) -> Optional[Locus]:
    try:
        return next(
            search(
                {
                    "query": {
                        "bool": {
                            "filter": {
                                "term": {"properties.ztf_object_id": ztf_object_id,},
                            },
                        },
                    },
                }
            )
        )
    except StopIteration:
        return None
