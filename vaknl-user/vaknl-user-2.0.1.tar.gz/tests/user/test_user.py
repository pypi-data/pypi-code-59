"""Tests for `vaknl_user/user/user.py`.

Created: 2020-07-14 (Merijn, DAT-1583)
Updated: 2020-07-14 (Merijn, DAT-1583)
"""


# ----------------------------------------------------------------------------------------------------------------------
# Import libraries
# ----------------------------------------------------------------------------------------------------------------------
import unittest


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
class UserMethodsTest(unittest.TestCase):
    """Test all the methods of the `user.user.User` dataclass."""

    # General attributes.
    nbc_api = NBC()
    firestore_client = user.utils.create_firestore_client(project_id='vaknldev')  # Don't test in prod environment!

    def setUp(self):
        """Sets up test case environment. Repeats for every separate test."""
        self.dmp_user_id = 'xxx'
        self.user = user.user.User(self.dmp_user_id)

    def tearDown(self):
        """Tears down test case environment. Repeats for every separate test."""
        self.dmp_user_id = None
        self.user = None

    def test_add_event(self):
        """Tests the `add_event()` method twice in a row."""
        # Add first event.
        n = self.user.statistics.general.event_cnt
        data = read_json('data/event/reservation/ReservationPersonalData.json')
        e = event.create_event(data)
        self.user.add_event(e, self.nbc_api)
        self.assertIsInstance(self.user, user.user.User)
        self.assertEqual(self.user.statistics.general.event_cnt, n + 1)

        # Add second event.
        data = read_json('data/event/filter/ProductPageFilterFlight.json')
        e = event.create_event(data)
        self.user.add_event(e, self.nbc_api)
        self.assertIsInstance(self.user, user.user.User)
        self.assertEqual(self.user.statistics.general.event_cnt, n + 2)

    def test_add_events(self):
        """Tests the `add_events()` method twice in a row."""
        # Add first events.
        n = self.user.statistics.general.event_cnt
        data = read_json('data/event/clickstream_event_list_sample_small.json')
        ee = event.event.Events()
        ee.add_raw_events(data)
        m = len(ee.event_list)
        self.user.add_events(ee, self.nbc_api)
        self.assertIsInstance(self.user, user.user.User)
        self.assertEqual(self.user.statistics.general.event_cnt, n + m)

        # Add second events.
        data = read_json('data/event/clickstream_event_list_sample_small.json')
        ee = event.event.Events()
        ee.add_raw_events(data)
        k = len(ee.event_list)
        self.user.add_events(ee, self.nbc_api)
        self.assertIsInstance(self.user, user.user.User)
        self.assertEqual(self.user.statistics.general.event_cnt, n + m + k)

    def test_add_raw_event(self):
        """Tests the `add_raw_event()` method twice in a row."""
        # Add first raw event.
        n = self.user.statistics.general.event_cnt
        data = read_json('data/event/reservation/ReservationPersonalData.json')
        self.user.add_raw_event(data, self.nbc_api)
        self.assertIsInstance(self.user, user.user.User)
        self.assertEqual(self.user.statistics.general.event_cnt, n + 1)

        # Add second raw event.
        data = read_json('data/event/filter/ProductPageFilterFlight.json')
        self.user.add_raw_event(data, self.nbc_api)
        self.assertIsInstance(self.user, user.user.User)
        self.assertEqual(self.user.statistics.general.event_cnt, n + 2)

    def test_add_raw_events(self):
        """Tests the `add_raw_events()` method twice in a row. Here, `data` is created from separate events, to avoid
        counting raw events in the raw data that are not converted to events later on."""
        # Add first raw events.
        n = self.user.statistics.general.event_cnt
        data_1 = read_json('data/event/pageview/PageviewProduct.json')
        data_2 = read_json('data/event/filter/ProductPageFilterAirport.json')
        data = [data_1, data_2]
        m = len(data)
        self.user.add_raw_events(data, self.nbc_api)
        self.assertIsInstance(self.user, user.user.User)
        self.assertEqual(self.user.statistics.general.event_cnt, n + m)

        # Add second raw events.
        data_1 = read_json('data/event/filter/GlobalFilterPartyComposition.json')
        data_2 = read_json('data/event/other/PriceClick.json')
        data_3 = read_json('data/event/reservation/ReservationExtras.json')
        data = [data_1, data_2, data_3]
        k = len(data)
        self.user.add_raw_events(data, self.nbc_api)
        self.assertIsInstance(self.user, user.user.User)
        self.assertEqual(self.user.statistics.general.event_cnt, n + m + k)

    def test_statistics_to_dict(self):
        """Test the `statistics_to_dict()` method."""
        # Check if dictionary.
        data = read_json('data/event/clickstream_event_list_sample_small.json')
        self.user.add_raw_events(data, self.nbc_api)
        d = self.user.statistics_to_dict()
        self.assertIsInstance(d, dict)

        # Check if the fields in `Statistics` and the keys in the dictionary have a one-on-one relationship.
        fields = ['general', 'other', 'product', 'reservation', 'search', 'session']
        for field in fields:
            self.assertTrue(field in d)
        self.assertTrue(len([field for field in d.keys() if field not in fields]) == 0)

        # Add field that does not belong.
        self.user.statistics.not_a_field = 0
        d = self.user.statistics_to_dict()
        self.assertIsInstance(d, dict)
        self.assertTrue('not_a_field' not in d)

    def test_statistics_from_dict(self):
        """Test the `statistics_from_dict()` method."""
        # Is equal to original.
        data = read_json('data/event/clickstream_event_list_sample_small.json')
        u = user.user.User(self.dmp_user_id)
        u.add_raw_events(data, self.nbc_api)
        d = u.statistics_to_dict()
        self.user.statistics_from_dict(d)
        self.assertEqual(self.user, u)

        # Add field that does not belong.
        d['not_a_field'] = 'I am not wanted.'
        self.user = user.user.User(self.dmp_user_id)
        self.user.statistics_from_dict(d)
        self.assertEqual(self.user, u)

    def test_import_statistics(self):
        """Test the `import_statistics()` method. For this test to work the `self.dmp_user_id` might have to be
        changed."""
        # The following `dmp_user_id` must exists in the `dmp_user` Firestore collection in order to import statistics.
        dmp_user_id = u'xxx'

        # Import statistics from Firestore.
        u = user.user.User(dmp_user_id)
        u.import_statistics(self.firestore_client)
        self.assertIsInstance(u, user.user.User)

    def test_export_statistics(self):
        """Test the `export_statistics()` method. For this test to work the `self.dmp_user_id` might have to be
        changed."""
        # The following `dmp_user_id` must not exists in the `dmp_user` Firestore collection in `vaknldev`, in order not
        # to overwrite existing data.
        dmp_user_id = u'dummy_id_that_should_not_exist'

        # Create user.
        data = read_json('data/event/clickstream_event_list_sample_small.json')
        u = user.user.User(dmp_user_id)
        u.add_raw_events(data, self.nbc_api)

        # Write to Firestore.
        u.export_statistics(self.firestore_client)

        # Read from Firestore and create user to compare.
        v = user.user.User(dmp_user_id)
        v.import_statistics(self.firestore_client)
        self.assertEqual(u, v)

        # Delete written document from Firestore.
        user.utils.delete_dmp_user_firestore(self.firestore_client, dmp_user_id)

    def test_create_user_from_clickstream(self):
        """Test the `create_user_from_clickstream()` method. For this test to work the `dmp_user_id` variable might
        have to be changed."""
        # The following `dmp_user_id` must exists in the `in_website_clickstream` Firestore collection in order to
        # import data.
        dmp_user_id = u'0:ehwlstzz:4Bw6YDlX5g9XAUgpol_6AIgYPBOWcMYf'

        # Create user by using by using import function form utilities and the `add_raw_events()` method.
        u = user.user.User(dmp_user_id)
        data = user.utils.import_website_clickstream_events(self.firestore_client, u.dmp_user_id)
        self.assertTrue(len(data) > 0)  # Make sure there is at least one event imported.
        u.add_raw_events(data, self.nbc_api)
        self.assertIsInstance(u, user.user.User)

        # Create user with `create_user_from_clickstream()` method.
        v = user.user.User(dmp_user_id)
        v.create_user_from_clickstream(self.firestore_client)
        self.assertIsInstance(v, user.user.User)
        self.assertEqual(u, v)

    def test_update_user_from_clickstream(self):
        """Test the `create_user_from_clickstream()` method. For this test to work the `dmp_user_id` variable might
        have to be changed."""
        # The following `dmp_user_id` must exists in the `in_website_clickstream` Firestore collection in order to
        # import data.
        dmp_user_id = u'0:ehwlstzz:4Bw6YDlX5g9XAUgpol_6AIgYPBOWcMYf'

        # Create user by using by using import function form utilities and the `add_raw_events()` method.
        u = user.user.User(dmp_user_id)
        data = user.utils.import_website_clickstream_events(self.firestore_client, u.dmp_user_id)
        u.add_raw_events(data, self.nbc_api)
        self.assertIsInstance(u, user.user.User)

        # Make sure there are at least two events with different timestamp for this user.
        min_timestamp = u.statistics.general.activity_first_timestamp
        self.assertNotEqual(min_timestamp, u.statistics.general.activity_last_timestamp)

        # Create user that is partially filled with the first event.
        ee = event.event.Events()
        ee.add_raw_events(data)
        ee.event_list = [e for e in ee.event_list if e.timestamp <= min_timestamp]
        v = user.user.User(dmp_user_id)
        v.add_events(ee, self.nbc_api)
        self.assertGreater(v.statistics.general.event_cnt, 0)  # Make sure there is at least one event added.

        # Check if `update_user_from_clickstream()` method updates the user in the same way.
        v.update_user_from_clickstream(self.firestore_client)
        self.assertEqual(u, v)


# ----------------------------------------------------------------------------------------------------------------------
# Command-line entry point
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
