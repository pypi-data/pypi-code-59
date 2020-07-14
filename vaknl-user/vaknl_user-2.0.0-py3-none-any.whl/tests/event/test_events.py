"""Test `Events` dataclass.

Performs unit tests on `vaknl_user.event.event.Events` dataclass functionality.

Created: 2020-07-01 (Merijn, DAT-1583)
Updated: 2020-07-12 (Merijn, DAT-1583)
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
class EventsGeneralTestCase(unittest.TestCase):
    """Test case for general functionality of `Events` dataclass`."""

    def test_blank_creation(self):
        """Test creating a blank instance."""
        ee = event.event.Events()
        self.assertIsInstance(ee, event.event.Events)
        self.assertEqual(ee.event_list, [])

    def test_merge(self):
        """Test `merge()` method."""
        file_path = 'data/event/clickstream_event_list_sample_small.json'
        data = read_json(file_path)
        ee = event.event.Events()
        ee.add_raw_events(clickstream_event_list=data)
        n = len(ee.event_list)
        ee.merge(ee)
        self.assertIsInstance(ee, event.event.Events)
        self.assertEqual(len(ee.event_list), 2*n)


class AddEventTestCase(unittest.TestCase):
    """Test case to check if `self.add_event()` method of the `vaknl_user.event.event.Events` dataclass works properly.
    Gets data on events from `data/event/` directory."""

    def add_event_tester(self, file_path: str):
        data = read_json(file_path)
        ee = event.event.Events()
        for event_data in data:
            ee.add_raw_event(clickstream_event_data=event_data)
            self.assertIsInstance(ee, event.event.Events)

    def test_1(self):
        file_path = 'data/event/clickstream_event_list_sample_small.json'
        self.add_event_tester(file_path)

    def test_2(self):
        file_path = 'data/event/clickstream_event_list_sample_large.json'
        self.add_event_tester(file_path)

    def test_3(self):
        file_path = 'data/event/clickstream_event_list_sample_huge_1.json'
        self.add_event_tester(file_path)

    def test_4(self):
        file_path = 'data/event/clickstream_event_list_sample_huge_2.json'
        self.add_event_tester(file_path)


class AddEventsTestCase(unittest.TestCase):
    """Test case to check if `self.add_events()` method of the `vaknl_user.event.event.Events` dataclass works properly.
    Gets data on events from `data/event/` directory."""

    def add_events_tester(self, file_path: str):
        data = read_json(file_path)
        ee = event.event.Events()
        ee.add_raw_events(clickstream_event_list=data)
        self.assertIsInstance(ee, event.event.Events)

    def test_1(self):
        file_path = 'data/event/clickstream_event_list_sample_small.json'
        self.add_events_tester(file_path)

    def test_2(self):
        file_path = 'data/event/clickstream_event_list_sample_large.json'
        self.add_events_tester(file_path)

    def test_3(self):
        file_path = 'data/event/clickstream_event_list_sample_huge_1.json'
        self.add_events_tester(file_path)

    def test_4(self):
        file_path = 'data/event/clickstream_event_list_sample_huge_2.json'
        self.add_events_tester(file_path)


# ----------------------------------------------------------------------------------------------------------------------
# Command-line entry point
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
