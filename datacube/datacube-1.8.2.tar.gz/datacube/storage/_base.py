from typing import Optional, Dict, Any, Tuple
from urllib.parse import urlparse

from datacube.model import Dataset
from datacube.utils.uris import uri_resolve, pick_uri


def _get_band_and_layer(b: Dict[str, Any]) -> Tuple[Optional[int], Optional[str]]:
    """ Encode legacy logic for extracting band/layer:

        on input:
        band -- Int | Nothing
        layer -- Str | Int | Nothing

    Valid combinations are:
        band  layer  Output
    ---------------------------
          -     -    ( - ,  - )
          -    int   (int,  - )
         int    -    (int,  - )
         int   str   (int, str)
          -    str   ( - , str)

    """
    band = b.get('band')
    layer = b.get('layer')

    if band is None:
        if isinstance(layer, int):
            return (layer, None)
        if layer is None or isinstance(layer, str):
            return (None, layer)

        raise ValueError('Expect `layer` to be one of None,int,str but it is {}'.format(type(layer)))
    else:
        if not isinstance(band, int):
            raise ValueError('Expect `band` to be an integer (it is {})'.format(type(band)))
        if layer is not None and not isinstance(layer, str):
            raise ValueError('Expect `layer` to be one of None,str but it is {}'.format(type(layer)))

        return (band, layer)


def _extract_driver_data(ds: Dataset) -> Optional[Any]:
    return ds.metadata_doc.get('driver_data', None)

def measurement_paths(ds: Dataset) -> Dict[str, str]:
    """
    Returns a dictionary mapping from band name to url pointing to band storage
    resource.

    :return: Band Name => URL
    """
    if ds.uris is None:
        raise ValueError('No locations on this dataset')

    base = pick_uri(ds.uris)
    return dict((k, uri_resolve(base, m.get('path')))
                for k, m in ds.measurements.items())


class BandInfo:
    __slots__ = ('name',
                 'uri',
                 'band',
                 'layer',
                 'dtype',
                 'nodata',
                 'units',
                 'crs',
                 'transform',
                 'center_time',
                 'format',
                 'driver_data')

    def __init__(self,
                 ds: Dataset,
                 band: str,
                 uri_scheme: Optional[str] = None):
        try:
            canonical_name = ds.type.canonical_measurement(band)
        except KeyError:
            raise ValueError('No such band: {}'.format(band))

        mm = ds.measurements.get(canonical_name)
        mp = ds.type.measurements.get(canonical_name)

        if mm is None or mp is None:
            raise ValueError('No such band: {}'.format(band))

        if ds.uris is None:
            raise ValueError('No uris defined on a dataset')

        base_uri = pick_uri(ds.uris, uri_scheme)

        bint, layer = _get_band_and_layer(mm)

        self.name = band
        self.uri = uri_resolve(base_uri, mm.get('path'))
        self.band = bint
        self.layer = layer
        self.dtype = mp.dtype
        self.nodata = mp.nodata
        self.units = mp.units
        self.crs = ds.crs
        self.transform = ds.transform
        self.format = ds.format
        self.driver_data = _extract_driver_data(ds)

    @property
    def uri_scheme(self) -> str:
        return urlparse(self.uri).scheme
