'''
This module runs tests on the creation and deletion of databases by
the amazedb.db module. It checks whether the databases are being created, 
the metadata being updated in real-time and dropping of databases and metadata updation afterwards.

WARNING: Tests should be run on empty database folders, otherwise they can mess with 
actual databases, and may delete them, resulting in permanent loss of the files.
'''
# Import required modules
import sys
import os

# Import the test runner module
import test_runner

# Switch our current directory
sys.path.append('..')
__path__ = ['..']
# Import the module to be tested
import dbms as db # pylint: disable=wrong-import-position

# Test 1: Check if the db is actually created
def _test1():
    d = db.create('testdb', dbPath='../')
    return 'dbms.db' in str(type(d))

# Test 2: Make sure that new databases don't have groups
def _test2():
    return db.db('testdb', dbPath='../').groups == []

# Test 3: Check if create method raises an error if it is given the wrong database directory
def _test3():
    db.create('testdb')

# Test 4: Check if db access method raises exception when it can't find the database directory
def _test4():
    db.db('testdb')

# Test 5: Check if safeMode prevents creation of a database that already exists
def _test5():
    d = db.create('testdb', dbPath='../')
    return 'dbms.db' in str(type(d))

# Test 6: Check whether disabled safeMode raises exception during
# creation of a database that already exists
def _test6():
    db.create('testdb', safeMode=False, dbPath='../')

# Test 7: Check if disabled safeMode raises exception when trying
# to access a database that does not exist
def _test7():
    db.db('abcd', safeMode=False, dbPath='../')

# Test 8: Check if safe mode creates a non-existent db when accessed
def _test8():
    d = db.db('abcd', dbPath='../')
    return 'dbms.db' in str(type(d))

# Test 9: Check if the getAllDbs method works properly
def _test9():
    return db.getAllDbs(dbPath='../') == ['abcd', 'testdb']

# Test 10: Trying to create db with invalid names shoud raise errors
def _test10():
    db.create('test*')

# Test 11: Trying to create db with invalid names shoud raise errors
def _test11():
    db.create('test.db')

# Test 12: Trying to create db with invalid names shoud raise errors
def _test12():
    db.db('test/directory')

# Test 13: Trying to create db with invalid names shoud raise errors
def _test13():
    db.db('test ')

# Test 14: Check if the drop method works properly
def _test14():
    for i in db.getAllDbs(dbPath="../"):
        db.db(i, dbPath="../").drop()
    return os.listdir('..//db') == []

# Create a new test suite with the test_runner.TestSuite class
tests = test_runner.TestSuite(name="Database creation/deletion tests", tests=[

    # Register all our tests with the test_runner.TestCase class
    test_runner.TestCase(_test1, name="Database Creates", op='isTrue'),
    test_runner.TestCase(_test2, name="No groups in new database", op='isTrue'),
    test_runner.TestCase(_test3, name="Creating DB on wrong path", op='exception', expectedVal='ValueError'),
    test_runner.TestCase(_test4, name="Accessing DB on wrong path", op='exception', expectedVal='ValueError'),
    test_runner.TestCase(_test5, name="safeMode prevents creation of existing DB", op='isTrue'),
    test_runner.TestCase(_test6, name="safeMode disabled raises error (Creation of existing DB)", op='exception', expectedVal='DBExistsError'),
    test_runner.TestCase(_test7, name="safeMode disabled raises error (Accessing non-existent DB)", op='exception', expectedVal='DBNotFoundError'),
    test_runner.TestCase(_test8, name="safeMode enabled creates non-existent DB", op='isTrue'),
    test_runner.TestCase(_test9, name="getAllDbs() method", op='isTrue'),
    test_runner.TestCase(_test10, name="Create DB with weird name 1", op="exception", expectedVal='ValueError'),
    test_runner.TestCase(_test11, name="Create DB with weird name 2", op="exception", expectedVal='ValueError'),
    test_runner.TestCase(_test12, name="Create DB with weird name 3", op="exception", expectedVal='ValueError'),
    test_runner.TestCase(_test13, name="Create DB with weird name 4", op="exception", expectedVal='ValueError'),
    test_runner.TestCase(_test14, name="Drop databases", op="isTrue")

])

if __name__ == "__main__":
    tests.run()
