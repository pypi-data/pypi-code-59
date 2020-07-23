'''
This module runs tests on the accessing of data stored inside groups.
It checks whether the data returned is correct and also checks the sort algorithms
and whether proper exceptions are raised when getting bad params.

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
    db = dbms.db('test-db', dbPath='..')
    grp = db.getGroup('testgrp')

    #Insert 10 sample data dicts
    for i in range(10):
        grp.insert({'a': i, 'b': 10-i})


# Cleanup tasks for the tests
def _cleanup():
    global db
    db.drop()


# Create a new test suite with the test_runner.TestSuite class
tests = test_runner.TestSuite(name="Data accessibility tests", setup=_setup, cleanup=_cleanup, tests=[

    # Register all our tests with the test_runner.TestCase class

    # First we will check fixed value filters
    test_runner.TestCase(
        lambda: grp.get({'a': 0}),
        expectedVal=[{'a': 0, 'b': 10}],
        name="Check Filter: Fixed value",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': 1, 'b': 9}),
        expectedVal=[{'a': 1, 'b': 9}],
        name="Check Filter: Fixed value (both)",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': 5, 'b': 4}),
        expectedVal=[],
        name="Check Filter: Empty return",
        op='eq'
    ),

    # Now some special filters
    test_runner.TestCase(
        lambda: grp.get({'a': {'__lt': 1}}),
        expectedVal=[{'a': 0, 'b': 10}],
        name="Check Filter: __lt",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__gt': 7}}),
        expectedVal=[{'a': 8, 'b': 2}, {'a': 9, 'b': 1}],
        name="Check Filter: __gt",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__gte': 8}}),
        expectedVal=[{'a': 8, 'b': 2}, {'a': 9, 'b': 1}],
        name="Check Filter: __gte",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__lte': 1}}),
        expectedVal=[{'a': 0, 'b': 10}, {'a': 1, 'b': 9}],
        name="Check Filter: __lte",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__re': "[41]"}}),
        expectedVal=[{'a': 1, 'b': 9}, {'a': 4, 'b': 6}],
        name="Check Filter: __re",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__ne': 9}}),
        expectedVal=[{'a': i, 'b': 10-i} for i in range(9)],
        name="Check Filter: __ne",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__cf': lambda x: x % 4 == 0}}),
        expectedVal=[{'a': 0, 'b': 10}, {'a': 4, 'b': 6}, {'a': 8, 'b': 2}],
        name="Check Filter: __cf",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__lte': 1, '__ne': 0}}),
        expectedVal=[{'a': 1, 'b': 9}],
        name="Check Filter: Misc",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__gte': 7, '__re': "[4-9]", '__ne': 9}}),
        expectedVal=[{'a': 7, 'b': 3}, {'a': 8, 'b': 2}],
        name="Check Filter: Misc",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__lte': 1}, 'b':9}),
        expectedVal=[{'a': 1, 'b': 9}],
        name="Mutltiple check args one custom one specific",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__lte': 8}, 'b': {'__lt': 3}}),
        expectedVal=[{'a': 8, 'b': 2}],
        name="Multiple check args both custom",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__gt': 6}, 'b': {'__gt': 9}}),
        expectedVal=[],
        name="Multiple check args both custom",
        op='eq'
    ),

    # Here we check the get_one method
    test_runner.TestCase(
        lambda: grp.get_one({'a': {'__lte': 8}}),
        expectedVal={'a': 0, 'b': 10},
        name="Check get_one method",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get_one({'a': {'__gte': 8}, 'b': {'__lte': 3}}),
        expectedVal={'a': 8, 'b': 2},
        name="Check get_one method",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get_one({'a': {'__gte': 10}}),
        expectedVal=None,
        name="Check get_one method",
        op='eq'
    ),

    # Now we check the sort method
    test_runner.TestCase(
        lambda: grp.get({'a': {'__gte': 8}}, sortby='b'),
        expectedVal=[{'a': 9, 'b': 1}, {'a': 8, 'b': 2}],
        name="Check sortby parameter",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__gte': 8}}, sortby='a'),
        expectedVal=[{'a': 8, 'b': 2}, {'a': 9, 'b': 1}],
        name="Check sortby parameter",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__gte': 10}}, sortby='a'),
        expectedVal=[],
        name="Check sortby on empty result",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get_one({'a': {'__gte': 8}}, sortby='b'),
        expectedVal={'a': 9, 'b': 1},
        name="Check sortby on get_one method",
        op='eq'
    ),
    test_runner.TestCase(
        lambda: grp.get_one({'a': {'__gte': 8}}, sortby='a'),
        expectedVal={'a': 8, 'b': 2},
        name="Check sortby on get_one method",
        op='eq'
    ),

    # Now we check if the proper errors are raised when giving wrong inputs
    test_runner.TestCase(
        lambda: grp.get({'a': {'__re': '{45}'}}),
        expectedVal='InvalidRegExpError',
        name="Check Invalid RegExp",
        op='exception'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__cf': lambda: 5}}),
        expectedVal='InvalidFilterError',
        name="Check Invalid custom function filter",
        op='exception'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'lte': 8}}),
        expectedVal='InvalidFilterError',
        name="Check invaild filter",
        op='exception'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__gte': 9, 'lte': 8}, 'b': {'__ne': 0}}),
        expectedVal='InvalidFilterError',
        name="Check invaild filter",
        op='exception'
    ),
    test_runner.TestCase(
        lambda: grp.get({'a': {'__lt': 10}, 'b': {'__gt': 1}}, sortby='c'),
        expectedVal='ValueError',
        name="Check invalid sort param",
        op='exception'
    ),
    test_runner.TestCase(
        lambda: grp.get_one({'a': 0, 'b': {'__gt': 1}}, sortby='c'),
        expectedVal='ValueError',
        name="Check invalid sort param on get one method",
        op='exception'
    )
])

if __name__ == "__main__":
    try:
        tests.run()
    except:
        pass
