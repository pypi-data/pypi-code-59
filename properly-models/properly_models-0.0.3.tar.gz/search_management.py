# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = person_id_from_dict(json.loads(json_string))
#     result = person_from_dict(json.loads(json_string))
#     result = search_id_from_dict(json.loads(json_string))
#     result = search_from_dict(json.loads(json_string))
#     result = users_search_id_from_dict(json.loads(json_string))
#     result = search_result_id_from_dict(json.loads(json_string))
#     result = search_result_from_dict(json.loads(json_string))
#     result = users_search_from_dict(json.loads(json_string))
#     result = simple_listing_id_from_dict(json.loads(json_string))
#     result = simple_listing_from_dict(json.loads(json_string))
#     result = search_notification_id_from_dict(json.loads(json_string))
#     result = search_notification_from_dict(json.loads(json_string))

from typing import List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


class SearchResult:
    id: 'SearchResult'
    results: List['SearchResult']
    search_as_of_millis: float
    search_id: str

    def __init__(self, id: 'SearchResult', results: List['SearchResult'], search_as_of_millis: float, search_id: str) -> None:
        self.id = id
        self.results = results
        self.search_as_of_millis = search_as_of_millis
        self.search_id = search_id

    @staticmethod
    def from_dict(obj: Any) -> 'SearchResult':
        assert isinstance(obj, dict)
        id = SearchResult.from_dict(obj.get("id"))
        results = from_list(SearchResult.from_dict, obj.get("results"))
        search_as_of_millis = from_float(obj.get("searchAsOfMillis"))
        search_id = from_str(obj.get("searchId"))
        return SearchResult(id, results, search_as_of_millis, search_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = to_class(SearchResult, self.id)
        result["results"] = from_list(lambda x: to_class(SearchResult, x), self.results)
        result["searchAsOfMillis"] = to_float(self.search_as_of_millis)
        result["searchId"] = from_str(self.search_id)
        return result


class Search:
    addresses: List[str]
    building_types: List[str]
    geohash6_areas: List[str]
    id: str
    last_run_millis: float
    max_price: float
    max_square_foot: float
    min_baths: float
    min_parking: float
    min_price: float
    min_square_foot: float
    neighbourhoods: List[str]
    properly_city_code: str
    search_hash: str

    def __init__(self, addresses: List[str], building_types: List[str], geohash6_areas: List[str], id: str, last_run_millis: float, max_price: float, max_square_foot: float, min_baths: float, min_parking: float, min_price: float, min_square_foot: float, neighbourhoods: List[str], properly_city_code: str, search_hash: str) -> None:
        self.addresses = addresses
        self.building_types = building_types
        self.geohash6_areas = geohash6_areas
        self.id = id
        self.last_run_millis = last_run_millis
        self.max_price = max_price
        self.max_square_foot = max_square_foot
        self.min_baths = min_baths
        self.min_parking = min_parking
        self.min_price = min_price
        self.min_square_foot = min_square_foot
        self.neighbourhoods = neighbourhoods
        self.properly_city_code = properly_city_code
        self.search_hash = search_hash

    @staticmethod
    def from_dict(obj: Any) -> 'Search':
        assert isinstance(obj, dict)
        addresses = from_list(from_str, obj.get("addresses"))
        building_types = from_list(from_str, obj.get("buildingTypes"))
        geohash6_areas = from_list(from_str, obj.get("geohash6Areas"))
        id = from_str(obj.get("id"))
        last_run_millis = from_float(obj.get("lastRunMillis"))
        max_price = from_float(obj.get("maxPrice"))
        max_square_foot = from_float(obj.get("maxSquareFoot"))
        min_baths = from_float(obj.get("minBaths"))
        min_parking = from_float(obj.get("minParking"))
        min_price = from_float(obj.get("minPrice"))
        min_square_foot = from_float(obj.get("minSquareFoot"))
        neighbourhoods = from_list(from_str, obj.get("neighbourhoods"))
        properly_city_code = from_str(obj.get("properlyCityCode"))
        search_hash = from_str(obj.get("searchHash"))
        return Search(addresses, building_types, geohash6_areas, id, last_run_millis, max_price, max_square_foot, min_baths, min_parking, min_price, min_square_foot, neighbourhoods, properly_city_code, search_hash)

    def to_dict(self) -> dict:
        result: dict = {}
        result["addresses"] = from_list(from_str, self.addresses)
        result["buildingTypes"] = from_list(from_str, self.building_types)
        result["geohash6Areas"] = from_list(from_str, self.geohash6_areas)
        result["id"] = from_str(self.id)
        result["lastRunMillis"] = to_float(self.last_run_millis)
        result["maxPrice"] = to_float(self.max_price)
        result["maxSquareFoot"] = to_float(self.max_square_foot)
        result["minBaths"] = to_float(self.min_baths)
        result["minParking"] = to_float(self.min_parking)
        result["minPrice"] = to_float(self.min_price)
        result["minSquareFoot"] = to_float(self.min_square_foot)
        result["neighbourhoods"] = from_list(from_str, self.neighbourhoods)
        result["properlyCityCode"] = from_str(self.properly_city_code)
        result["searchHash"] = from_str(self.search_hash)
        return result


class UsersSearch:
    id: str
    last_run_millis: float
    last_run_search_result_id: str
    search_data: Search
    search_id: str
    user_id: str

    def __init__(self, id: str, last_run_millis: float, last_run_search_result_id: str, search_data: Search, search_id: str, user_id: str) -> None:
        self.id = id
        self.last_run_millis = last_run_millis
        self.last_run_search_result_id = last_run_search_result_id
        self.search_data = search_data
        self.search_id = search_id
        self.user_id = user_id

    @staticmethod
    def from_dict(obj: Any) -> 'UsersSearch':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        last_run_millis = from_float(obj.get("lastRunMillis"))
        last_run_search_result_id = from_str(obj.get("lastRunSearchResultId"))
        search_data = Search.from_dict(obj.get("searchData"))
        search_id = from_str(obj.get("searchId"))
        user_id = from_str(obj.get("userId"))
        return UsersSearch(id, last_run_millis, last_run_search_result_id, search_data, search_id, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["lastRunMillis"] = to_float(self.last_run_millis)
        result["lastRunSearchResultId"] = from_str(self.last_run_search_result_id)
        result["searchData"] = to_class(Search, self.search_data)
        result["searchId"] = from_str(self.search_id)
        result["userId"] = from_str(self.user_id)
        return result


class SimpleListing:
    address: str
    bathrooms: float
    bathrooms_half: float
    bedrooms: float
    brokerage: str
    id: str
    image_medium_url: str
    image_thumbnail_url: str
    image_url: str
    list_price: float
    parking: float
    predicted_price: float
    square_feet: float

    def __init__(self, address: str, bathrooms: float, bathrooms_half: float, bedrooms: float, brokerage: str, id: str, image_medium_url: str, image_thumbnail_url: str, image_url: str, list_price: float, parking: float, predicted_price: float, square_feet: float) -> None:
        self.address = address
        self.bathrooms = bathrooms
        self.bathrooms_half = bathrooms_half
        self.bedrooms = bedrooms
        self.brokerage = brokerage
        self.id = id
        self.image_medium_url = image_medium_url
        self.image_thumbnail_url = image_thumbnail_url
        self.image_url = image_url
        self.list_price = list_price
        self.parking = parking
        self.predicted_price = predicted_price
        self.square_feet = square_feet

    @staticmethod
    def from_dict(obj: Any) -> 'SimpleListing':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        bathrooms = from_float(obj.get("bathrooms"))
        bathrooms_half = from_float(obj.get("bathroomsHalf"))
        bedrooms = from_float(obj.get("bedrooms"))
        brokerage = from_str(obj.get("brokerage"))
        id = from_str(obj.get("id"))
        image_medium_url = from_str(obj.get("imageMediumUrl"))
        image_thumbnail_url = from_str(obj.get("imageThumbnailUrl"))
        image_url = from_str(obj.get("imageUrl"))
        list_price = from_float(obj.get("listPrice"))
        parking = from_float(obj.get("parking"))
        predicted_price = from_float(obj.get("predictedPrice"))
        square_feet = from_float(obj.get("squareFeet"))
        return SimpleListing(address, bathrooms, bathrooms_half, bedrooms, brokerage, id, image_medium_url, image_thumbnail_url, image_url, list_price, parking, predicted_price, square_feet)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["bathrooms"] = to_float(self.bathrooms)
        result["bathroomsHalf"] = to_float(self.bathrooms_half)
        result["bedrooms"] = to_float(self.bedrooms)
        result["brokerage"] = from_str(self.brokerage)
        result["id"] = from_str(self.id)
        result["imageMediumUrl"] = from_str(self.image_medium_url)
        result["imageThumbnailUrl"] = from_str(self.image_thumbnail_url)
        result["imageUrl"] = from_str(self.image_url)
        result["listPrice"] = to_float(self.list_price)
        result["parking"] = to_float(self.parking)
        result["predictedPrice"] = to_float(self.predicted_price)
        result["squareFeet"] = to_float(self.square_feet)
        return result


class Person:
    id: str
    unverified_email: str
    verified_email: str

    def __init__(self, id: str, unverified_email: str, verified_email: str) -> None:
        self.id = id
        self.unverified_email = unverified_email
        self.verified_email = verified_email

    @staticmethod
    def from_dict(obj: Any) -> 'Person':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        unverified_email = from_str(obj.get("unverifiedEmail"))
        verified_email = from_str(obj.get("verifiedEmail"))
        return Person(id, unverified_email, verified_email)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["unverifiedEmail"] = from_str(self.unverified_email)
        result["verifiedEmail"] = from_str(self.verified_email)
        return result


class SearchNotification:
    changed_results: List[SimpleListing]
    id: str
    new_results: List[SimpleListing]
    search: Search
    searcher: Person
    unsubscribe_url: str

    def __init__(self, changed_results: List[SimpleListing], id: str, new_results: List[SimpleListing], search: Search, searcher: Person, unsubscribe_url: str) -> None:
        self.changed_results = changed_results
        self.id = id
        self.new_results = new_results
        self.search = search
        self.searcher = searcher
        self.unsubscribe_url = unsubscribe_url

    @staticmethod
    def from_dict(obj: Any) -> 'SearchNotification':
        assert isinstance(obj, dict)
        changed_results = from_list(SimpleListing.from_dict, obj.get("changedResults"))
        id = from_str(obj.get("id"))
        new_results = from_list(SimpleListing.from_dict, obj.get("newResults"))
        search = Search.from_dict(obj.get("search"))
        searcher = Person.from_dict(obj.get("searcher"))
        unsubscribe_url = from_str(obj.get("unsubscribeUrl"))
        return SearchNotification(changed_results, id, new_results, search, searcher, unsubscribe_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["changedResults"] = from_list(lambda x: to_class(SimpleListing, x), self.changed_results)
        result["id"] = from_str(self.id)
        result["newResults"] = from_list(lambda x: to_class(SimpleListing, x), self.new_results)
        result["search"] = to_class(Search, self.search)
        result["searcher"] = to_class(Person, self.searcher)
        result["unsubscribeUrl"] = from_str(self.unsubscribe_url)
        return result


def person_id_from_dict(s: Any) -> str:
    return from_str(s)


def person_id_to_dict(x: str) -> Any:
    return from_str(x)


def person_from_dict(s: Any) -> Person:
    return Person.from_dict(s)


def person_to_dict(x: Person) -> Any:
    return to_class(Person, x)


def search_id_from_dict(s: Any) -> str:
    return from_str(s)


def search_id_to_dict(x: str) -> Any:
    return from_str(x)


def search_from_dict(s: Any) -> Search:
    return Search.from_dict(s)


def search_to_dict(x: Search) -> Any:
    return to_class(Search, x)


def users_search_id_from_dict(s: Any) -> str:
    return from_str(s)


def users_search_id_to_dict(x: str) -> Any:
    return from_str(x)


def search_result_id_from_dict(s: Any) -> str:
    return from_str(s)


def search_result_id_to_dict(x: str) -> Any:
    return from_str(x)


def search_result_from_dict(s: Any) -> SearchResult:
    return SearchResult.from_dict(s)


def search_result_to_dict(x: SearchResult) -> Any:
    return to_class(SearchResult, x)


def users_search_from_dict(s: Any) -> UsersSearch:
    return UsersSearch.from_dict(s)


def users_search_to_dict(x: UsersSearch) -> Any:
    return to_class(UsersSearch, x)


def simple_listing_id_from_dict(s: Any) -> str:
    return from_str(s)


def simple_listing_id_to_dict(x: str) -> Any:
    return from_str(x)


def simple_listing_from_dict(s: Any) -> SimpleListing:
    return SimpleListing.from_dict(s)


def simple_listing_to_dict(x: SimpleListing) -> Any:
    return to_class(SimpleListing, x)


def search_notification_id_from_dict(s: Any) -> str:
    return from_str(s)


def search_notification_id_to_dict(x: str) -> Any:
    return from_str(x)


def search_notification_from_dict(s: Any) -> SearchNotification:
    return SearchNotification.from_dict(s)


def search_notification_to_dict(x: SearchNotification) -> Any:
    return to_class(SearchNotification, x)
