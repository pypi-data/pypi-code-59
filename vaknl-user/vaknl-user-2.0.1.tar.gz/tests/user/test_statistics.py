"""Tests for `vaknl_user/user/statistics.py`.

Created: 2020-07-12 (Merijn, DAT-1583)
Updated: 2020-07-12 (Merijn, DAT-1583)
"""

# TODO: Unittests for all other class methods or functions.

# ----------------------------------------------------------------------------------------------------------------------
# Import libraries
# ----------------------------------------------------------------------------------------------------------------------
import unittest
from dacite import from_dict


# ----------------------------------------------------------------------------------------------------------------------
# Import internal modules
# ----------------------------------------------------------------------------------------------------------------------
from vaknl_NBC import NBC
from vaknl_user import event
from vaknl_user import user
from tests.utils import read_json


# ----------------------------------------------------------------------------------------------------------------------
# Test classes
# ----------------------------------------------------------------------------------------------------------------------
class StatisticsMethodsTest(unittest.TestCase):

    nbc_api = NBC()
    base_data = read_json('data/event/other/Session.json')
    base_event = event.create_event(base_data)

    def setUp(self):
        """Sets up test case environment. Repeats for every separate test."""
        self.statistics = user.statistics.Statistics()
        self.statistics.add_event(self.base_event, self.nbc_api)

    def tearDown(self):
        """Tears down test case environment. Repeats for every separate test."""
        self.statistics = None

    def test_add_event(self):
        """Tests the `add_event()` method twice in a row."""
        # Add first event.
        n = self.statistics.general.event_cnt
        data = read_json('data/event/reservation/ReservationPersonalData.json')
        e = event.create_event(data)
        self.statistics.add_event(e, self.nbc_api)
        self.assertIsInstance(self.statistics, user.statistics.Statistics)
        self.assertEqual(self.statistics.general.event_cnt, n + 1)

        # Add second event.
        data = read_json('data/event/filter/ProductPageFilterFlight.json')
        e = event.create_event(data)
        self.statistics.add_event(e, self.nbc_api)
        self.assertIsInstance(self.statistics, user.statistics.Statistics)
        self.assertEqual(self.statistics.general.event_cnt, n + 2)

    def test_add_events(self):
        """Tests the `add_events()` method twice in a row."""
        # Add first events.
        n = self.statistics.general.event_cnt
        data = read_json('data/event/clickstream_event_list_sample_small.json')
        ee = event.event.Events()
        ee.add_raw_events(data)
        m = len(ee.event_list)
        self.statistics.add_events(ee, self.nbc_api)
        self.assertIsInstance(self.statistics, user.statistics.Statistics)
        self.assertEqual(self.statistics.general.event_cnt, n + m)

        # Add second events.
        data = read_json('data/event/clickstream_event_list_sample_large.json')
        ee = event.event.Events()
        ee.add_raw_events(data)
        k = len(ee.event_list)
        self.statistics.add_events(ee, self.nbc_api)
        self.assertIsInstance(self.statistics, user.statistics.Statistics)
        self.assertEqual(self.statistics.general.event_cnt, n + m + k)

    def test_to_dict(self):
        """Tests the `to_dict()` method."""
        d = self.statistics.to_dict()
        s = from_dict(data_class=user.statistics.Statistics, data=d)
        self.assertEqual(s, self.statistics)

    def test_validate(self):
        """Tests the `validate()` method."""
        # TODO: Test validate() method.
        pass

    def test_update_funnel_step(self):
        """Tests the `update_funnel_step()` method after adding several different funnel events."""
        # Test base user with only one `Session` event.
        self.assertEqual(self.statistics.general.funnel_step, 'visitor')

        # Test change to 'active'.
        data = read_json('data/event/filter/GlobalFilterPartyComposition.json')
        e = event.create_event(data)
        self.statistics.add_event(e, self.nbc_api, update_funnel_step=False)
        self.assertEqual(self.statistics.general.funnel_step, 'visitor')
        self.statistics.update_funnel_step()
        self.assertEqual(self.statistics.general.funnel_step, 'active')

        # Test change to 'active_plus'.
        data = read_json('data/event/filter/ProductPageFilterFlight.json')
        e = event.create_event(data)
        self.statistics.add_event(e, self.nbc_api, update_funnel_step=False)
        self.assertEqual(self.statistics.general.funnel_step, 'active')
        self.statistics.update_funnel_step()
        self.assertEqual(self.statistics.general.funnel_step, 'active_plus')

        # Test change to 'in_market'.
        data = read_json('data/event/reservation/ReservationPersonalData.json')
        e = event.create_event(data)
        self.statistics.add_event(e, self.nbc_api, update_funnel_step=False)
        self.assertEqual(self.statistics.general.funnel_step, 'active_plus')
        self.statistics.update_funnel_step()
        self.assertEqual(self.statistics.general.funnel_step, 'in_market')

        # Test change to 'booked'.
        data = read_json('data/event/reservation/ReservationBooked.json')
        e = event.create_event(data)
        self.statistics.add_event(e, self.nbc_api, update_funnel_step=False)
        self.assertEqual(self.statistics.general.funnel_step, 'in_market')
        self.statistics.update_funnel_step()
        self.assertEqual(self.statistics.general.funnel_step, 'booked')


# ----------------------------------------------------------------------------------------------------------------------
# Command-line entry point
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
