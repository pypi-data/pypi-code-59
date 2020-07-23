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
import os
import json

# Import the test runner module
import test_runner

# Switch our current directory
sys.path.append('..')
__path__ = ['..']

# Import the module to be tested
import dbms # pylint: disable=wrong-import-position

global db

# Setup tasks for the tests
def _setup():
    global db
    # Create a database for our testing of the groups
    db = dbms.db('test-db', dbPath='../') 

# Test 1: Check if the group is actually created
def _test1():
    global db
    db.createGroup('testgrp')
    return 'testgrp.group' in os.listdir(f'../db/{db.name}')

# Test 2: Trying to create groups with invalid names shoud raise errors
def _test2():
    global db
    db.createGroup('test*')

# Test 3: Trying to create groups with invalid names shoud raise errors
def _test3():
    global db
    db.createGroup('test.db')

# Test 4: Trying to create groups with invalid names shoud raise errors
def _test4():
    global db
    db.createGroup('test/directory')

# Test 5: Trying to create groups with invalid names shoud raise errors
def _test5():
    global db
    db.createGroup('test ')

# Test 6: Trying to create already existing group with safeMode disabled
def _test6():
    global db
    db.createGroup('testgrp', safeMode=False)

# Test 7: Trying to create already existing group with safeMode enabled
def _test7():
    global db
    d = db.createGroup('testgrp')
    return 'group.group' in str(type(d))

# Test 8: Trying to add more groups and then check if the parent db's group list is updated or not
def _test8():
    global db
    db.createGroup('test2')
    db.createGroup('test3')
    db.createGroup('test4')
    db.createGroup('test5')
    return db.groups == ['testgrp', 'test2', 'test3', 'test4', 'test5']

# Test 9: Check if the metadata file is updated on new group creation
def _test9():
    global db
    d = {}
    with open(f'../db/{db.name}/metadata.json', 'r') as f:
        d = json.loads(f.read())
    return d['groups'] == ['testgrp', 'test2', 'test3', 'test4', 'test5']

# Test 10: Trying to get a group
def _test10():
    global db
    d = db.getGroup('testgrp')
    return 'group.group' in str(type(d))

# Test 11: Trying to get a group that does not exists but safeMode enabled
def _test11():
    global db
    d = db.getGroup('test8')
    return 'group.group' in str(type(d))

# Test 12: Trying to get a group that does not exists but safeMode disabled
def _test12():
    global db
    db.getGroup('testgr8', safeMode=False)

# Test 13: Trying to delete a group and check if the in-mem list is updated
def _test13():
    global db
    db.getGroup('testgrp').drop()
    return 'testgrp' not in db.groups

# Delete a group and check if the metadata file is updated
def _test14():
    global db
    db.getGroup('test2').drop()
    g = False
    with open('../db/test-db/metadata.json', 'r') as f:
        g = 'test2' not in json.loads(f.read())['groups']
    return g

# Cleanup tasks for the tests
def _cleanup():
    global db
    db.drop()

# Create a new test suite with the test_runner.TestSuite class
tests = test_runner.TestSuite(name="Group creation/deletion tests",setup=_setup, cleanup=_cleanup, tests=[

    # Register all our tests with the test_runner.TestCase class
    test_runner.TestCase(_test1, name="Group Creates", op='isTrue'),
    test_runner.TestCase(_test2, name="Create group with weird name 1", op="exception", expectedVal='ValueError'),
    test_runner.TestCase(_test3, name="Create group with weird name 2", op="exception", expectedVal='ValueError'),
    test_runner.TestCase(_test4, name="Create group with weird name 3", op="exception", expectedVal='ValueError'),
    test_runner.TestCase(_test5, name="Create group with weird name 4", op="exception", expectedVal='ValueError'),
    test_runner.TestCase(_test6, name="Create already existing group with safeMode disabled", op="exception", expectedVal='GroupExistsError'),
    test_runner.TestCase(_test7, name="Create already existing group with safeMode enabled", op="isTrue"),
    test_runner.TestCase(_test8, name="Parent db's in-mem metadata update", op="isTrue"),
    test_runner.TestCase(_test9, name="Metadata file updates on new group", op="isTrue"),
    test_runner.TestCase(_test10, name="Get a group", op="isTrue"),
    test_runner.TestCase(_test11, name="Get a non-existent group with safeMode enabled", op="isTrue"),
    test_runner.TestCase(_test12, name="Get a non-existent group with safeMode disabled", op="exception", expectedVal='GroupNotFoundError'),
    test_runner.TestCase(_test13, name="Drop a group", op="isTrue"),
    test_runner.TestCase(_test14, name="Drop a group and check metadata file", op="isTrue")
])

if __name__ == "__main__":
    try:
        tests.run()
    except:
        pass
