"""
PySTAC is a library for working with SpatioTemporal Asset Catalogs (STACs)
"""

# flake8: noqa


class STACError(Exception):
    """A STACError is raised for errors relating to STAC, e.g. for
    invalid formats or trying to operate on a STAC that does not have
    the required information available.
    """
    pass


from pystac.version import (__version__, STAC_VERSION)
from pystac.stac_io import STAC_IO
from pystac.extensions import Extensions
from pystac.stac_object import STACObject
from pystac.media_type import MediaType
from pystac.link import (Link, LinkType)
from pystac.catalog import (Catalog, CatalogType)
from pystac.collection import (Collection, Extent, SpatialExtent, TemporalExtent, Provider)
from pystac.item import (Item, Asset, CommonMetadata)
from pystac.item_collection import ItemCollection

from pystac.serialization import (STACObjectType, stac_object_from_dict)

STAC_IO.stac_object_from_dict = stac_object_from_dict

from pystac import extensions
import pystac.extensions.commons
import pystac.extensions.eo
import pystac.extensions.label
import pystac.extensions.view

STAC_EXTENSIONS = extensions.base.RegisteredSTACExtensions([
    extensions.commons.COMMONS_EXTENSION_DEFINITION,
    extensions.eo.EO_EXTENSION_DEFINITION,
    extensions.label.LABEL_EXTENSION_DEFINITION,
    extensions.view.VIEW_EXTENSION_DEFINITION,
])


def read_file(href):
    """Reads a STAC object from a file.

    This method will return either a Catalog, a Collection, or an Item based on what the
    file contains.

    This is a convenience method for :meth:`STACObject.from_file <pystac.STACObject.from_file>`

    Args:
        href (str): The HREF to read the object from.

    Returns:
        The specific STACObject implementation class that is represented
        by the JSON read from the file located at HREF.
    """
    return STACObject.from_file(href)


def write_file(obj, include_self_link=True, dest_href=None):
    """Writes a STACObject to a file.

    This will write only the Catalog, Collection or Item ``obj``. It will not attempt
    to write any other objects that are linked to ``obj``; if you'd like functinoality to
    save off catalogs recursively see :meth:`Catalog.save <pystac.Catalog.save>`.

    This method will write the JSON of the object to the object's assigned "self" link or
    to the dest_href if provided. To set the self link, see :meth:`STACObject.set_self_href
    <pystac.STACObject.set_self_href>`.

    Convenience method for :meth:`STACObject.from_file <pystac.STACObject.from_file>`

    Args:
        obj (STACObject): The STACObject to save.
        include_self_link (bool): If this is true, include the 'self' link with this object.
            Otherwise, leave out the self link.
        dest_href (str): Optional HREF to save the file to. If None, the object will be saved
            to the object's self href.
    """
    obj.save_object(include_self_link=include_self_link, dest_href=dest_href)
