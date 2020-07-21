from dataclasses import dataclass
from datetime import datetime
from typing import Union, Tuple

from .open_area import OpenArea
from .location_taxonomy import LocationTaxonomy


@dataclass(frozen=True, eq=False)
class Vessel:
    imo: int
    name: str
    vessel_class: str
    ice_class: str
    year_built: int
    deadweight: int
    length_overall: float
    breadth_extreme: int
    market_deployment: str
    push_type: str
    open_port: str
    open_date: datetime
    operational_status: str
    commercial_operator: str
    commercial_status: str
    eta: datetime
    last_fixed: int
    latest_ais: datetime
    subclass: str
    willing_to_switch_subclass: bool
    open_prediction_accuracy: str
    open_areas: Tuple[OpenArea, ...]
    availability_port_type: str
    availability_date_type: str
    liquid_capacity: int
    fixture_type: str
    last_cargoes: str
    last_cargo_types: Tuple[int, ...]
    eta_at_open_port: datetime

    def __post_init__(self):
        if self.open_areas is None:
            object.__setattr__(self, 'open_areas', tuple())
        if self.last_cargo_types is None:
            object.__setattr__(self, 'last_cargo_types', tuple())

    @property
    def open_country(self) -> Union[str, None]:
        return self.__area_name_by_taxonomy(LocationTaxonomy.COUNTRY)

    @property
    def open_narrow_area(self) -> Union[str, None]:
        return self.__area_name_by_taxonomy(LocationTaxonomy.NARROW_AREA)

    @property
    def open_wide_area(self) -> Union[str, None]:
        return self.__area_name_by_taxonomy(LocationTaxonomy.WIDE_AREA)

    def __area_name_by_taxonomy(self, taxonomy: str) -> Union[str, None]:
        for a in self.open_areas:
            if a.location_taxonomy == taxonomy:
                return a.name
        return None
