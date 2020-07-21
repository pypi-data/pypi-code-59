from typing import List

import astropy.timeseries
import pandas as pd
from marshmallow import post_load
from marshmallow_jsonapi import fields, Schema

from .fields import IncludeRelated, Lightcurve
from ..utils import mjd_to_datetime


class AlertSchema(Schema):
    class Meta:
        type_ = "alert"

    id = fields.String(attribute="alert_id")
    properties = fields.Dict()
    mjd = fields.Float()
    resource_meta = fields.ResourceMeta()
    document_meta = fields.DocumentMeta()

    @post_load
    def make_alert(self, data: dict, **kwargs):
        return Alert(**data)


class LocusSchema(Schema):
    class Meta:
        type_ = "locus"

    id = fields.Str(attribute="locus_id")
    htm16 = fields.Int()
    ra = fields.Float()
    dec = fields.Float()
    properties = fields.Dict()
    lightcurve = Lightcurve()
    alerts = IncludeRelated(AlertSchema, many=True)
    tags = fields.List(fields.Str())
    catalogs = fields.List(fields.Str())
    catalog_matches = fields.List(fields.Dict())
    resource_meta = fields.ResourceMeta()
    document_meta = fields.DocumentMeta()

    @post_load
    def make_locus(self, data: dict, **kwargs):
        return Locus(**data)


class LocusListingSchema(Schema):
    class Meta:
        type_ = "locus_listing"

    id = fields.Str(attribute="locus_id")
    htm16 = fields.Int()
    ra = fields.Float()
    dec = fields.Float()
    properties = fields.Dict()
    locus = IncludeRelated(LocusSchema, many=False)
    alerts = IncludeRelated(AlertSchema, many=True)
    tags = fields.List(fields.Str())
    catalogs = fields.List(fields.Dict())
    resource_meta = fields.ResourceMeta()
    document_meta = fields.DocumentMeta()

    @post_load
    def make_locus(self, data, **kwargs):
        return data["locus"]


class Alert:
    def __init__(self, alert_id: str, mjd: float, properties: dict, **kwargs):
        self.alert_id = alert_id
        self.mjd = mjd
        self.properties = properties


class Locus:
    def __init__(
        self,
        locus_id: str,
        ra: float,
        dec: float,
        properties: dict,
        tags: List[str],
        lightcurve: pd.DataFrame,
        alerts: List[Alert],
        catalogs: List[str] = None,
        catalog_objects: List[dict] = None,
        watch_list_ids: List[str] = None,
        watch_object_ids: List[str] = None,
        **kwargs
    ):
        self.locus_id = locus_id
        self.ra = ra
        self.dec = dec
        self.properties = properties
        self.tags = tags
        self.lightcurve = lightcurve
        self.catalogs = catalogs
        self.alerts = alerts
        if self.catalogs is None:
            self.catalogs = []
        self.catalog_objects = catalog_objects
        if self.catalog_objects is None:
            self.catalog_objects = []
        self.watch_list_ids = watch_list_ids
        if self.watch_list_ids is None:
            self.watch_list_ids = []
        self.watch_object_ids = watch_object_ids
        if self.watch_object_ids is None:
            self.watch_object_ids = []
        self._timeseries = None

    @staticmethod
    def get_by_ztf_object_id(ztf_object_id: str):
        pass

    @property
    def timeseries(self):
        if self._timeseries:
            return self._timeseries
        self._timeseries = astropy.timeseries.TimeSeries(
            data=[alert.properties for alert in self.alerts],
            time=[mjd_to_datetime(alert.mjd) for alert in self.alerts],
        )
        return self._timeseries
