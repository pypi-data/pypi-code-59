"""Test `create_event()`.

Performs unit tests on `vaknl_user.event.create_event()` function.

Created: 2020-07-01 (Merijn, DAT-1583)
Updated: 2020-07-11 (Merijn, DAT-1583)
"""


# ----------------------------------------------------------------------------------------------------------------------
# Import libraries
# ----------------------------------------------------------------------------------------------------------------------
import unittest
import os

from vaknl_user import event
from tests.utils import read_json


# ----------------------------------------------------------------------------------------------------------------------
# Test classes
# ----------------------------------------------------------------------------------------------------------------------
# class SearchPageSearchQueryTestCase(unittest.TestCase):
#
#     def test_default_filters(self):
#         with open('data/event/event_value_json_search_page_search_query_default_filters.json') as json_file:
#             self.event_value_json = json.load(json_file)
#
#         base_event = event.event.Event(event_id='fergw43gverv', timestamp=426452754, dmp_session_id='0:rgtw5wetrbf')
#         e = event._create_event_search_page_search_query(base_event, self.event_value_json)
#         self.assertIsInstance(e, event.other.SearchPageSearchQuery)
#
#     def test_custom_filters(self):
#         with open('data/event/event_value_json_search_page_search_query_custom_filters.json') as json_file:
#             self.event_value_json = json.load(json_file)
#
#         base_event = event.event.Event(event_id='fergw43gverv', timestamp=426452754, dmp_session_id='0:rgtw5wetrbf')
#         e = event._create_event_search_page_search_query(base_event, self.event_value_json)
#         self.assertIsInstance(e, event.other.SearchPageSearchQuery)


class CreateSpecificEventTestCase(unittest.TestCase):
    """Test case to check if `vaknl_user.event.create_event()` function creates specific events correctly. Gets data on
    events from `data/event/` directory.

    Note: The following events are missing from the data files:
        event.pageview.PageviewBlog
        event.pageview.PageviewDeal
        event.pageview.PageviewKeuzehulp
        event.pageview.PageviewOther
        event.other.KeuzehulpShowTop10
    """

    def event_category_tester(self, event_category: str):
        _module = __import__(f'vaknl_user.event.{event_category}', fromlist=['object'])
        dir_path = f'data/event/{event_category}'
        for file in os.listdir(dir_path):
            if file.endswith(".json"):
                file_path = os.path.join(dir_path, file)
                event_name = os.path.basename(file_path).replace('.json', '')
                event_dataclass = getattr(_module, event_name)
                event_data = read_json(file_path)
                e = event.create_event(data=event_data)
                self.assertIsInstance(e, event_dataclass)

    def test_filter(self):
        self.event_category_tester('filter')

    def test_other(self):
        self.event_category_tester('other')

    def test_pageview(self):
        self.event_category_tester('pageview')

    def test_reservation(self):
        self.event_category_tester('reservation')


class CreateEventsFromClickstreamTestCase(unittest.TestCase):
    """Test case to check if `vaknl_user.event.create_event()` function can create a list of events from a list of raw
    clickstream data. Gets data from `data/event/` directory."""

    def clickstream_events_tester(self, file_path: str):
        data = read_json(file_path)
        for event_data in data:
            e = event.create_event(event_data)
            if e is not None:
                self.assertIsInstance(e, event.event.Event)

    def test_1(self):
        file_path = 'data/event/clickstream_event_list_sample_small.json'
        self.clickstream_events_tester(file_path)

    def test_2(self):
        file_path = 'data/event/clickstream_event_list_sample_large.json'
        self.clickstream_events_tester(file_path)

    def test_3(self):
        file_path = 'data/event/clickstream_event_list_sample_huge_1.json'
        self.clickstream_events_tester(file_path)

    def test_4(self):
        file_path = 'data/event/clickstream_event_list_sample_huge_2.json'
        self.clickstream_events_tester(file_path)


# ----------------------------------------------------------------------------------------------------------------------
# Command-line entry point
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
