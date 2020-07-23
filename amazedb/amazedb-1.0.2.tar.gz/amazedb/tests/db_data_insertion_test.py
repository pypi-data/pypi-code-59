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

# Test 1: Check if the data is actually inserted
def _test1():
    global grp
    return grp.insert({'a': 0, 'b': 10})

# Test 2: Check inserta_many function
def _test2():
    global grp
    return grp.insert_many(*[{'a': i, 'b': 10-i} for i in range(1, 10)])

# Test 3: Check if the data inserted is accesible
def _test3():
    exp = []
    for i in range(10):
        exp.append({'a': i, 'b': 10-i})
    return grp.get({}) == exp

# Test 4: preLoad argument
def _test4():
    global grp
    grp = db.getGroup('testgrp', preLoad=True)
    return grp.data[0]

# Test 5: Insertion in preLoad mode
def _test5():
    global grp
    grp.insert(a=10, b=11)
    return {'a': 10, 'b': 11} in grp.data

# Test 6: Insert many in preLoad mode
def _test6():
    global grp
    data = []
    for i in range(11, 20):
        data.append({'a': i, 'b': 10})
    grp.insert_many(*data)

    mat = True
    for i in data:
        if i not in grp.data:
            mat = False
            break
    return mat

# Test 7: Check if data inserted in preLoad mode was saved to the file
def _test7():
    grp = db.getGroup('testgrp')
    return grp.get({'a': {'__gt': 11, '__lt': 15}})

# Cleanup tasks for the tests
def _cleanup():
    global db
    db.drop()


# Create a new test suite with the test_runner.TestSuite class
tests = test_runner.TestSuite(name="Data insertion tests", setup=_setup, cleanup=_cleanup, tests=[

    # Register all our tests with the test_runner.TestCase class
    test_runner.TestCase(_test1, name="Check insert method", op='isTrue'),
    test_runner.TestCase(_test2, name="Check insert_many", op='isTrue'),
    test_runner.TestCase(_test3, name="Check data accesibility", op='isTrue'),
    test_runner.TestCase(
        _test4,
        name="Check data in preLoad mode",
        op='eq',
        expectedVal={'a': 0, 'b': 10}
    ),
    test_runner.TestCase(
        _test5,
        name="Insert data in preLoad mode",
        op='isTrue'
    ),
    test_runner.TestCase(
        _test6,
        name="Insert multiple data in preLoad mode",
        op='isTrue'
    ),
    test_runner.TestCase(
        _test7,
        name="Check data saved through preLoad mode",
        op='eq',
        expectedVal=[
            {'a': 12, 'b': 10},
            {'a': 13, 'b': 10},
            {'a': 14, 'b': 10}
        ]
    ),

])


if __name__ == "__main__":
    try:
        tests.run()
    except:
        pass
