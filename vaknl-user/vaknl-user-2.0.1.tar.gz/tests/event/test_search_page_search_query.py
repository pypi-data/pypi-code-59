"""Test `create_event()`.

Performs unit tests on `vaknl_user.event.create_event()` function.

Created: 2020-07-01 (Merijn, DAT-1583)
Updated: 2020-07-11 (Merijn, DAT-1583)
"""


# ----------------------------------------------------------------------------------------------------------------------
# Import libraries
# ----------------------------------------------------------------------------------------------------------------------
import unittest

from vaknl_user import event
from tests.utils import read_json


# ----------------------------------------------------------------------------------------------------------------------
# Test classes
# ----------------------------------------------------------------------------------------------------------------------
class SearchPageSearchQueryTestCase(unittest.TestCase):

    def test_default_filters(self):
        event_value = read_json('data/event/event_value_json_search_page_search_query_default_filters.json')
        e = event.other.SearchPageSearchQuery(
            event_id='fergw43gverv',
            timestamp=426452754,
            dmp_session_id='0:rgtw5wetrbf',
            event_value=event_value
        )
        self.assertIsInstance(e, event.other.SearchPageSearchQuery)

    def test_custom_filters(self):
        event_value = read_json('data/event/event_value_json_search_page_search_query_custom_filters.json')
        e = event.other.SearchPageSearchQuery(
            event_id='fergw43gverv',
            timestamp=426452754,
            dmp_session_id='0:rgtw5wetrbf',
            event_value=event_value
        )
        self.assertIsInstance(e, event.other.SearchPageSearchQuery)


# ----------------------------------------------------------------------------------------------------------------------
# Command-line entry point
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
