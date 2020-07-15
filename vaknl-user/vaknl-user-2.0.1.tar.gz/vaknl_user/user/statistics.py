"""User statistics.

Contains dataclasses that keep track of several statistics when events are added.

Created: 2020-03-0? (Merijn)
Updated: 2020-07-14 (Merijn, DAT-1583)
"""

# TODO: improve section headers and structure.


# ----------------------------------------------------------------------------------------------------------------------
# Import libraries
# ----------------------------------------------------------------------------------------------------------------------
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Union
from datetime import datetime


# ----------------------------------------------------------------------------------------------------------------------
# Import internal modules
# ----------------------------------------------------------------------------------------------------------------------
from vaknl_user import event
from vaknl_NBC import NBC


# ----------------------------------------------------------------------------------------------------------------------
# Statistic super dataclass
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class Statistic:
    # TODO: docstring.

    def add_event(self, e: event.event.Event, nbc_api: NBC):
        # TODO: docstring.
        pass

    def validate(self):
        # TODO: docstring.
        pass


# ----------------------------------------------------------------------------------------------------------------------
# Field label information dataclasses
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class LabelInfo:
    # TODO: docstring.
    count: int = 0
    frequency: Dict[Any, int] = field(default_factory=dict)
    last: Union[str, int, None] = None

    def add_label(self, label: Union[str, int]):
        # TODO: docstring.
        self.last = label
        if label is not None:
            label = str(label)
            self.count += 1
            self.frequency[label] = self.frequency[label] + 1 if label in self.frequency else 1


@dataclass
class LabelListInfo:
    # TODO: docstring.
    frequency: Dict[Any, int] = field(default_factory=dict)

    def add_labels(self, labels: List[Union[str, int]]):
        # TODO: docstring.
        for label in labels:
            label = str(label)
            self.frequency[label] = self.frequency[label] + 1 if label in self.frequency else 1


# ----------------------------------------------------------------------------------------------------------------------
# Specific sub-sub dataclass
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class SearchPageSearchQueryStatistics(Statistic):
    # TODO: docstring.
    budget: LabelInfo = field(default_factory=LabelInfo)
    count: int = 0
    departure_airports: LabelListInfo = field(default_factory=LabelListInfo)
    departure_date: LabelInfo = field(default_factory=LabelInfo)
    departure_date_flex: LabelInfo = field(default_factory=LabelInfo)
    distance_to_beach: LabelInfo = field(default_factory=LabelInfo)
    durations: LabelListInfo = field(default_factory=LabelListInfo)
    geo: LabelListInfo = field(default_factory=LabelListInfo)
    meal_plans: LabelListInfo = field(default_factory=LabelListInfo)
    min_hotel_rating: LabelInfo = field(default_factory=LabelInfo)
    min_star_rating: LabelInfo = field(default_factory=LabelInfo)
    party_composition: LabelInfo = field(default_factory=LabelInfo)
    theme: LabelInfo = field(default_factory=LabelInfo)

    def add_event(self, e: event.event.Event, nbc_api: NBC):
        if isinstance(e, event.other.SearchPageSearchQuery):
            self.count += 1

            # Fields with LabelInfo.
            self.budget.add_label(e.budget)
            self.departure_date.add_label(e.departure_date)
            self.departure_date_flex.add_label(e.departure_date_flex)
            self.distance_to_beach.add_label(e.distance_to_beach)
            self.min_hotel_rating.add_label(e.min_hotel_rating)
            self.min_star_rating.add_label(e.min_star_rating)
            self.party_composition.add_label(e.party_composition)
            self.theme.add_label(e.theme)

            # Fields with LabelListInfo
            self.departure_airports.add_labels(e.departure_airports)
            self.durations.add_labels(e.durations)
            self.geo.add_labels(e.geo)
            self.meal_plans.add_labels(e.meal_plans)


# ----------------------------------------------------------------------------------------------------------------------
# Statistics sub dataclasses used in Statistics
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class GeneralStatistics(Statistic):
    # TODO: docstring.
    activity_first_timestamp: int = None
    activity_last_timestamp: int = None
    event_cnt: int = field(default=0)
    funnel_step: str = None  # = 'visitor'; the funnel names could change
    pageview_cnt: int = field(default=0)
    user_identifiers: Dict[str, List] = field(default_factory=dict)

    def add_event(self, e: event.event.Event, nbc_api: NBC):
        # TODO: docstring.
        t = e.timestamp
        self.activity_first_timestamp = min(elem for elem in [self.activity_first_timestamp, t] if elem is not None)
        self.activity_last_timestamp = max(elem for elem in [self.activity_last_timestamp, t] if elem is not None)
        self.event_cnt += 1 if isinstance(e, event.event.Event) else 0
        self.pageview_cnt += 1 if isinstance(e, event.pageview.Pageview) else 0
        if isinstance(e, event.other.SfmcId):
            if e.email and e.email != 'undefined':
                self.user_identifiers['email'] = list(set(self.user_identifiers.get('email', []) + [e.email]))

    def validate(self):
        # TODO: docstring.
        # TODO: dynamic default check.
        return (
                self.activity_first_timestamp is not None
                and self.activity_last_timestamp is not None
                and self.funnel_step is not None
                and self.event_cnt > 0
        )


@dataclass
class OtherStatistics(Statistic):
    # TODO: docstring.
    filter_party_composition_freq: Dict = field(default_factory=dict)
    keuzehulp_show_top10_cnt: int = field(default=0)

    def add_event(self, e: event.event.Event, nbc_api: NBC):
        # TODO: docstring.
        if isinstance(e, event.filter.GlobalFilterPartyComposition):
            self.filter_party_composition_freq[e.label] = self.filter_party_composition_freq[e.label] + 1 \
                if e.label in self.filter_party_composition_freq else 1
        self.keuzehulp_show_top10_cnt += 1 if isinstance(e, event.other.KeuzehulpShowTop10) else 0


@dataclass
class ProductStatistics(Statistic):
    # TODO: docstring.
    availability_check_cnt: int = field(default=0)
    filter_airport_cnt: int = field(default=0)
    filter_departure_date_cnt: int = field(default=0)
    filter_meal_plan_cnt: int = field(default=0)
    filter_flight_cnt: int = field(default=0)
    image_click_cnt: int = field(default=0)
    giata_id: LabelInfo = field(default_factory=LabelInfo)
    price_click_cnt: int = field(default=0)
    service_cnt: int = field(default=0)

    # NBC:
    country_code: LabelInfo = field(default_factory=LabelInfo)
    region_id: LabelInfo = field(default_factory=LabelInfo)
    city_id: LabelInfo = field(default_factory=LabelInfo)
    theme: LabelListInfo = field(default_factory=LabelListInfo)

    def add_event(self, e: event.event.Event, nbc_api: NBC):
        # TODO: docstring.
        self.availability_check_cnt += 1 if isinstance(e, event.other.ProductAvailability) else 0
        self.filter_airport_cnt += 1 if isinstance(e, event.filter.ProductPageFilterAirport) else 0
        self.filter_departure_date_cnt += 1 if isinstance(e, event.filter.ProductPageFilterDepDate) else 0
        self.filter_meal_plan_cnt += 1 if isinstance(e, event.filter.ProductPageFilterMealPlan) else 0
        self.filter_flight_cnt += 1 if isinstance(e, event.filter.ProductPageFilterFlight) else 0
        self.image_click_cnt += 1 if isinstance(e, event.other.ImageClick) else 0
        self.price_click_cnt += 1 if isinstance(e, event.other.PriceClick) else 0
        self.service_cnt += 1 if isinstance(e, event.other.ProductService) else 0
        if isinstance(e, event.pageview.PageviewProduct):
            self.giata_id.add_label(e.giata_id)
            data = nbc_api.get_by_giata_id(int(e.giata_id))
            if data:
                self.country_code.add_label(data.get('country_code'))
                self.region_id.add_label(data.get('region_id'))
                self.city_id.add_label(data.get('city_id'))
                themes = [
                    key for key, value in data.items() if ('theme_' in key) and (key != 'theme_main') and int(value)
                ]
                self.theme.add_labels(themes)


@dataclass
class ReservationStatistics(Statistic):
    # TODO: docstring.
    booking: LabelInfo = field(default_factory=LabelInfo)
    extras_cnt: int = field(default=0)
    extras_select_extras_cnt: int = field(default=0)
    overview_cnt: int = field(default=0)
    pageview_cnt: int = field(default=0)
    personal_data_cnt: int = field(default=0)
    reservation_id_freq: List[str] = field(default_factory=list)

    def add_event(self, e: event.event.Event, nbc_api: NBC):
        # TODO: docstring.
        if isinstance(e, event.reservation.ReservationBooked):
            if e.reservation_id not in self.reservation_id_freq and e.reservation_id is not None:
                self.reservation_id_freq.append(e.reservation_id)
                self.booking.add_label(e.giata_id)
        self.extras_cnt += 1 if isinstance(e, event.reservation.ReservationExtras) else 0
        self.extras_select_extras_cnt += 1 if isinstance(e, event.other.SelectExtrasBookingStep) else 0
        self.overview_cnt += 1 if isinstance(e, event.reservation.ReservationOverview) else 0
        self.pageview_cnt += 1 if isinstance(e, event.pageview.PageviewBookingStep) else 0
        self.personal_data_cnt += 1 if isinstance(e, event.reservation.ReservationPersonalData) else 0


@dataclass
class SearchStatistics(Statistic):
    # TODO: docstring.
    filter_select_cnt: int = field(default=0)
    pageview_cnt: int = field(default=0)
    search_query: SearchPageSearchQueryStatistics = field(default_factory=SearchPageSearchQueryStatistics)

    def add_event(self, e: event.event.Event, nbc_api: NBC):
        # TODO: docstring.
        self.filter_select_cnt += 1 if isinstance(e, event.filter.SearchPageFilter) else 0
        self.pageview_cnt += 1 if isinstance(e, event.pageview.PageviewSearch) else 0
        self.search_query.add_event(e, nbc_api)


@dataclass
class SessionStatistics(Statistic):
    # TODO: docstring.
    count: int = field(default=0)
    day_of_week_freq: LabelInfo = field(default_factory=LabelInfo)
    dmp_session_id_list: List[str] = field(default_factory=list)
    hour_of_day_freq: LabelInfo = field(default_factory=LabelInfo)

    def add_event(self, e: event.event.Event, nbc_api: NBC):
        # TODO: docstring.
        self.dmp_session_id_list = list(set(self.dmp_session_id_list + [e.dmp_session_id]))
        self.count = len(self.dmp_session_id_list)
        if isinstance(e, event.other.Session):
            date_time = datetime.fromtimestamp(e.timestamp / 1e3)
            self.day_of_week_freq.add_label(date_time.weekday())  # Day of week as number: 0-6 (Monday-Sunday)
            self.hour_of_day_freq.add_label(date_time.hour)


# ----------------------------------------------------------------------------------------------------------------------
# Statistics dataclass used in User
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class Statistics:
    # TODO: docstring.
    general: GeneralStatistics = field(default_factory=GeneralStatistics)
    other: OtherStatistics = field(default_factory=OtherStatistics)
    product: ProductStatistics = field(default_factory=ProductStatistics)
    reservation: ReservationStatistics = field(default_factory=ReservationStatistics)
    search: SearchStatistics = field(default_factory=SearchStatistics)
    session: SessionStatistics = field(default_factory=SessionStatistics)

    def add_event(self, e: event.event.Event, nbc_api: NBC = None, update_funnel_step=True):
        # TODO: docstring.
        if nbc_api is None:
            nbc_api = NBC()
        self.general.add_event(e, nbc_api)
        self.other.add_event(e, nbc_api)
        self.product.add_event(e, nbc_api)
        self.reservation.add_event(e, nbc_api)
        self.search.add_event(e, nbc_api)
        self.session.add_event(e, nbc_api)
        if update_funnel_step:
            self.update_funnel_step()

    def add_events(self, ee: event.event.Events, nbc_api: NBC = None):
        # TODO: docstring.
        ee.sort_by_timestamp_ascending()
        if nbc_api is None:
            nbc_api = NBC()
        for item in ee.event_list:
            self.add_event(item, nbc_api, update_funnel_step=False)
        self.update_funnel_step()

    def validate(self):
        # TODO: docstring.
        # TODO: include other checks.
        result = self.general.validate()
        return result

    def to_dict(self):
        """Get dictionary of fields. All nested dataclasses should be converted to dictionaries as well."""
        return asdict(self)

    def update_funnel_step(self):
        # TODO: docstring.

        # TODO: add ppcVisitorAcco, which is a funnel event.

        current_step = self.general.funnel_step
        if current_step != 'booked':
            if self.reservation.booking.count > 0:
                self.general.funnel_step = 'booked'
            elif current_step != 'in_market':
                if (
                        self.reservation.personal_data_cnt + self.reservation.overview_cnt
                        + self.reservation.extras_select_extras_cnt
                ) > 0:
                    self.general.funnel_step = 'in_market'
                elif current_step != 'active_plus':
                    if self.product.availability_check_cnt or self.product.filter_airport_cnt or \
                            self.product.filter_flight_cnt or self.product.filter_meal_plan_cnt or \
                            self.product.service_cnt or self.reservation.extras_cnt or \
                            self.product.image_click_cnt >= 5:
                        self.general.funnel_step = 'active_plus'
                    elif current_step != 'active':
                        if self.search.search_query.departure_date.count or self.product.filter_departure_date_cnt or \
                                bool(self.other.filter_party_composition_freq) or \
                                self.other.keuzehulp_show_top10_cnt or self.product.image_click_cnt >= 3 or \
                                self.search.filter_select_cnt >= 2:
                            self.general.funnel_step = 'active'
                        else:
                            self.general.funnel_step = 'visitor'
