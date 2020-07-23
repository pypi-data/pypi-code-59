'''
This module runs tests on the creation of groups by the utils.amazedb.db module.
It checks whether the groups are being created, the metadata being updated in
real-time and dropping of groups and metadata updation afterwards.

WARNING: Tests should be run on empty database folders, otherwise they can mess with
actual databases, and may delete them, resulting in permanent loss of the files.
'''

# pylint: disable=invalid-name
# pylint: disable=global-variable-undefined
# Import required modules
import sys

# Import the test runner module
import test_runner

# Switch our current directory
sys.path.append('..')
__path__ = ['..']

# Import the module to be tested
import dbms # pylint: disable=wrong-import-position

global db, grp

# Setup tasks for the tests
def _setup():
    global db, grp

    # Create a database for our testing of the groups
    db = dbms.db('test-db', dbPath='../')
    grp = db.getGroup('testgrp')
    grp.insert_many(*[{'a': i, 'b': 10-i} for i in range(10)])

# These tests are not the first ones to run,
# but they actually check the preLoad
# arguments. All others are far below
def _test1():
    global grp, db
    # Delete the old group
    grp.drop()
    # Load newer in preload mode
    grp = db.getGroup('testgrp', preLoad=True)
    # Insert sample data into it
    grp.insert_many(*[{'a': i, 'b': 10-i} for i in range(10)])

    grp.update({'a': 0}, {'a': 11})
    return {'a': 11, 'b': 10} in grp.data

def _test2():
    grp.update({'a': {'__re': "[4-6]"}}, {'a': 11})
    for i in [{'a': 11, 'b': 6}, {'a': 11, 'b': 5}, {'a': 11, 'b': 4}]:
        if i not in grp.data:
            return False
    return True

def _test3():
    grp.update({'a': {'__lte': 3}}, {'a': 11})
    for i in [{'a': 11, 'b': 9}, {'a': 11, 'b': 8}, {'a': 11, 'b': 7}]:
        if i not in grp.data:
            return False
    return True

def _test4():
    grp.update(
        {'a': {'__gt': 6, '__ne': 11}, 'b': {'__lte': 2}},
        {'a': -14}
        )
    for i in [{'a': -14, 'b': 2}, {'a': -14, 'b': 1}]:
        if i not in grp.data:
            return False
    return True

def _test5():
    grp.update(
        {'a': {'__gt': 6, '__ne': 11}, 'b': {'__lte': 4}},
        {'a': 12, 'b': 4, 'c': 8}
        )
    return {'a': 12, 'b': 4, 'c': 8} in grp.data

def _test6():
    grp.update_one({'a': 11}, {'b': 5, 'c': 4})
    return {'a': 11, 'b': 5, 'c': 4} in grp.data

def _test7():
    grp.update_one({'a': {'__gte': 11, '__lte': 11}}, {'b': 7, 'c': -11})
    return {'a': 11, 'b': 7, 'c': -11} in grp.data

# Cleanup tasks for the tests
def _cleanup():
    global db
    db.drop()


# Create a new test suite with the test_runner.TestSuite class
tests = test_runner.TestSuite(name="Data manipulation tests", setup=_setup, cleanup=_cleanup, tests=[

    # Register all our tests with the test_runner.TestCase class

    # Call all update functions
    test_runner.TestCase(
        lambda: grp.update({'a': 0}, {'a': 11}),
        expectedVal=1,
        name="Update single value",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.update({'a': {'__re': "[4-6]"}}, {'a': 11}),
        expectedVal=3,
        name="Update multiple values using __re filter",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.update({'a': {'__lte': 3}}, {'a': 11}),
        expectedVal=3,
        name="Update multiplpe values using multiple filters",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.update(
            {'a': {'__gt': 6, '__ne': 11}, 'b': {'__lte': 2}},
            {'a': -14}
            ),
        expectedVal=2,
        name="Update multiple values using multiple params",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.update(
            {'a': {'__gt': 6, '__ne': 11}, 'b': {'__lte': 4}},
            {'a': 12, 'b': 4, 'c': 8}
            ),
        expectedVal=1,
        name="Update and add new params",
        op='eq'
    ),

    # Test when update is called on empty input
    test_runner.TestCase(
        lambda: grp.update(
            {'a': -1},
            {'a': 12, 'b': 4, 'c': 8}
            ),
        expectedVal=0,
        name="Updating with filters matching no documents",
        op='eq'
    ),

    # Check the updated values.
    # WARNING: It is assumed that you have already
    # ran the group.get method tests, located in
    # db_data_get_test.py file
    test_runner.TestCase(
        lambda: len(grp.get({'a': 11})),
        expectedVal=7,
        name="Check updated values",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: len(grp.get({'c': 8})),
        expectedVal=1,
        name="Check updated values",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: len(grp.get({'a': -14, 'b': 4})),
        expectedVal=0,
        name="Check updated values",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: len(grp.get({'a': -14})),
        expectedVal=2,
        name="Check updated values",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.update_one({'a': 11}, {'b': 5, 'c': 4}),
        expectedVal=None,
        name="Update one method",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.update_one({'a': {'__gte': 11, '__lte': 11}}, {'b': 7, 'c': -11}),
        expectedVal=None,
        name="Update one method",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.get_one({'b': 5, 'c': 4}),
        expectedVal={'a': 11, 'b': 5, 'c': 4},
        name="Check updated values",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.get_one({'b': 7, 'c': -11}),
        expectedVal={'a': 11, 'b': 7, 'c': -11},
        name="Check updated values",
        op='eq'
    ),

    test_runner.TestCase(
        _test1,
        name="Update single value (preLoad mode)",
        op='isTrue'
    ),

    test_runner.TestCase(
        _test2,
        name="Update multiple values using __re filter (preLoad mode)",
        op='isTrue'
    ),

    test_runner.TestCase(
        _test3,
        name="Update multiplpe values using multiple filters (preLoad mode)",
        op='isTrue'
    ),

    test_runner.TestCase(
        _test4,
        name="Update multiple values using multiple params (preLoad mode)",
        op='isTrue'
    ),

    test_runner.TestCase(
        _test5,
        name="Update and add new params (preLoad mode)",
        op='isTrue'
    ),

    test_runner.TestCase(
        _test6,
        name="Update one method (preLoad mode)",
        op='isTrue'
    ),

    test_runner.TestCase(
        _test7,
        name="Update one method (preLoad mode)",
        op='isTrue'
    ),

    # Next up we'll run the deletion tests
    test_runner.TestCase(
        lambda: grp.remove({'a': {'__lt': 12, '__gt': 10}}),
        expectedVal=7,
        name="Delete values from database group using fiters",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.remove({'c': 8}),
        expectedVal=1,
        name="Delete values from database group using direct value",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.remove({'a': -14, 'b': 4}),
        expectedVal=0,
        name="Delete values from database group using multiple filters",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.remove_one({'a': -14}),
        expectedVal=None,
        name="Test remove one method",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: grp.remove_one({'a': {'__gt': -100, '__lt': 0}}),
        expectedVal=None,
        name="Test remove one method using filters",
        op='eq'
    ),

    test_runner.TestCase(
        lambda: len(grp.get({})),
        expectedVal=0,
        name="Check if all documents deleted",
        op='eq'
    )
])

if __name__ == "__main__":
    try:
        tests.run()
    except:
        pass
