# Copyright 2018 John Reese
# Licensed under the MIT license
import asyncio
import sqlite3
import sys
from pathlib import Path
from sqlite3 import OperationalError
from unittest import SkipTest, skipIf, skipUnless

import aiounittest

import aiosqlite

from .helpers import setup_logger

TEST_DB = Path("test.db")

# pypy uses non-standard text factory for low-level sqlite implementation
try:
    from _sqlite3 import _unicode_text_factory as default_text_factory
except ImportError:
    default_text_factory = str


class SmokeTest(aiounittest.AsyncTestCase):
    @classmethod
    def setUpClass(cls):
        setup_logger()

    def setUp(self):
        if TEST_DB.exists():
            TEST_DB.unlink()

    def tearDown(self):
        if TEST_DB.exists():
            TEST_DB.unlink()

    async def test_connection_await(self):
        db = await aiosqlite.connect(TEST_DB)
        self.assertIsInstance(db, aiosqlite.Connection)

        async with db.execute("select 1, 2") as cursor:
            rows = await cursor.fetchall()
            self.assertEqual(rows, [(1, 2)])

        await db.close()

    async def test_connection_context(self):
        async with aiosqlite.connect(TEST_DB) as db:
            self.assertIsInstance(db, aiosqlite.Connection)

            async with db.execute("select 1, 2") as cursor:
                rows = await cursor.fetchall()
                self.assertEqual(rows, [(1, 2)])

    async def test_connection_locations(self):
        class Fake:  # pylint: disable=too-few-public-methods
            def __str__(self):
                return str(TEST_DB)

        locs = ("test.db", b"test.db", Path("test.db"), Fake())

        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute("create table foo (i integer, k integer)")
            await db.execute("insert into foo (i, k) values (1, 5)")
            await db.commit()

            cursor = await db.execute("select * from foo")
            rows = await cursor.fetchall()

        for loc in locs:
            async with aiosqlite.connect(loc) as db:
                cursor = await db.execute("select * from foo")
                self.assertEqual(await cursor.fetchall(), rows)

    async def test_multiple_connections(self):
        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute(
                "create table multiple_connections "
                "(i integer primary key asc, k integer)"
            )

        async def do_one_conn(i):
            async with aiosqlite.connect(TEST_DB) as db:
                await db.execute("insert into multiple_connections (k) values (?)", [i])
                await db.commit()

        await asyncio.gather(*[do_one_conn(i) for i in range(10)])

        async with aiosqlite.connect(TEST_DB) as db:
            cursor = await db.execute("select * from multiple_connections")
            rows = await cursor.fetchall()

        assert len(rows) == 10

    async def test_multiple_queries(self):
        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute(
                "create table multiple_queries "
                "(i integer primary key asc, k integer)"
            )

            await asyncio.gather(
                *[
                    db.execute("insert into multiple_queries (k) values (?)", [i])
                    for i in range(10)
                ]
            )

            await db.commit()

        async with aiosqlite.connect(TEST_DB) as db:
            cursor = await db.execute("select * from multiple_queries")
            rows = await cursor.fetchall()

        assert len(rows) == 10

    async def test_iterable_cursor(self):
        async with aiosqlite.connect(TEST_DB) as db:
            cursor = await db.cursor()
            await cursor.execute(
                "create table iterable_cursor " "(i integer primary key asc, k integer)"
            )
            await cursor.executemany(
                "insert into iterable_cursor (k) values (?)", [[i] for i in range(10)]
            )
            await db.commit()

        async with aiosqlite.connect(TEST_DB) as db:
            cursor = await db.execute("select * from iterable_cursor")
            rows = []
            async for row in cursor:
                rows.append(row)

        assert len(rows) == 10

    async def test_context_cursor(self):
        async with aiosqlite.connect(TEST_DB) as db:
            async with db.cursor() as cursor:
                await cursor.execute(
                    "create table context_cursor "
                    "(i integer primary key asc, k integer)"
                )
                await cursor.executemany(
                    "insert into context_cursor (k) values (?)",
                    [[i] for i in range(10)],
                )
                await db.commit()

        async with aiosqlite.connect(TEST_DB) as db:
            async with db.execute("select * from context_cursor") as cursor:
                rows = []
                async for row in cursor:
                    rows.append(row)

        assert len(rows) == 10

    async def test_cursor_return_self(self):
        async with aiosqlite.connect(TEST_DB) as db:
            cursor = await db.cursor()

            result = await cursor.execute(
                "create table test_cursor_return_self (i integer, k integer)"
            )
            self.assertEqual(result, cursor, "cursor execute returns itself")

            result = await cursor.executemany(
                "insert into test_cursor_return_self values (?, ?)", [(1, 1), (2, 2)]
            )
            self.assertEqual(result, cursor)

            result = await cursor.executescript(
                "insert into test_cursor_return_self values (3, 3);"
                "insert into test_cursor_return_self values (4, 4);"
                "insert into test_cursor_return_self values (5, 5);"
            )
            self.assertEqual(result, cursor)

    async def test_connection_properties(self):
        async with aiosqlite.connect(TEST_DB) as db:
            self.assertEqual(db.total_changes, 0)

            async with db.cursor() as cursor:
                self.assertFalse(db.in_transaction)
                await cursor.execute(
                    "create table test_properties "
                    "(i integer primary key asc, k integer, d text)"
                )
                await cursor.execute(
                    "insert into test_properties (k, d) values (1, 'hi')"
                )
                self.assertTrue(db.in_transaction)
                await db.commit()
                self.assertFalse(db.in_transaction)

            self.assertEqual(db.total_changes, 1)

            self.assertIsNone(db.row_factory)
            self.assertEqual(db.text_factory, default_text_factory)

            async with db.cursor() as cursor:
                await cursor.execute("select * from test_properties")
                row = await cursor.fetchone()
                self.assertIsInstance(row, tuple)
                self.assertEqual(row, (1, 1, "hi"))
                with self.assertRaises(TypeError):
                    _ = row["k"]

            db.row_factory = aiosqlite.Row
            db.text_factory = bytes
            self.assertEqual(db.row_factory, aiosqlite.Row)
            self.assertEqual(db.text_factory, bytes)

            async with db.cursor() as cursor:
                await cursor.execute("select * from test_properties")
                row = await cursor.fetchone()
                self.assertIsInstance(row, aiosqlite.Row)
                self.assertEqual(row[1], 1)
                self.assertEqual(row[2], b"hi")
                self.assertEqual(row["k"], 1)
                self.assertEqual(row["d"], b"hi")

    async def test_fetch_all(self):
        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute(
                "create table test_fetch_all (i integer primary key asc, k integer)"
            )
            await db.execute(
                "insert into test_fetch_all (k) values (10), (24), (16), (32)"
            )
            await db.commit()

        async with aiosqlite.connect(TEST_DB) as db:
            cursor = await db.execute("select k from test_fetch_all where k < 30")
            rows = await cursor.fetchall()
            self.assertEqual(rows, [(10,), (24,), (16,)])

    async def test_enable_load_extension(self):
        """Assert that after enabling extension loading, they can be loaded"""
        async with aiosqlite.connect(TEST_DB) as db:
            try:
                await db.enable_load_extension(True)
                await db.load_extension("test")
            except OperationalError as e:
                assert "not authorized" not in e.args
            except AttributeError:
                raise SkipTest(
                    "python was not compiled with sqlite3 "
                    "extension support, so we can't test it"
                )

    async def test_set_progress_handler(self):
        """Assert that after setting a progress handler returning 1, DB operations are aborted"""
        async with aiosqlite.connect(TEST_DB) as db:
            await db.set_progress_handler(lambda: 1, 1)
            with self.assertRaises(OperationalError):
                await db.execute(
                    "create table test_progress_handler (i integer primary key asc, k integer)"
                )

    async def test_create_function(self):
        """Assert that after creating a custom function, it can be used"""

        def no_arg():
            return "no arg"

        def one_arg(num):
            return num * 2

        async with aiosqlite.connect(TEST_DB) as db:
            await db.create_function("no_arg", 0, no_arg)
            await db.create_function("one_arg", 1, one_arg)

            async with db.execute("SELECT no_arg();") as res:
                row = await res.fetchone()
                self.assertEqual(row[0], "no arg")

            async with db.execute("SELECT one_arg(10);") as res:
                row = await res.fetchone()
                self.assertEqual(row[0], 20)

    async def test_set_trace_callback(self):
        statements = []

        def callback(statement: str):
            statements.append(statement)

        async with aiosqlite.connect(TEST_DB) as db:
            await db.set_trace_callback(callback)

            await db.execute("select 10")
            self.assertIn("select 10", statements)

    async def test_connect_error(self):
        bad_db = Path("/something/that/shouldnt/exist.db")
        with self.assertRaisesRegex(OperationalError, "unable to open database"):
            async with aiosqlite.connect(bad_db) as db:
                self.assertIsNone(db)  # should never be reached

        with self.assertRaisesRegex(OperationalError, "unable to open database"):
            db = await aiosqlite.connect(bad_db)
            self.assertIsNone(db)  # should never be reached

    async def test_iterdump(self):
        async with aiosqlite.connect(":memory:") as db:
            await db.execute("create table foo (i integer, k charvar(250))")
            await db.executemany(
                "insert into foo values (?, ?)", [(1, "hello"), (2, "world")]
            )

            lines = [line async for line in db.iterdump()]
            self.assertEqual(
                lines,
                [
                    "BEGIN TRANSACTION;",
                    "CREATE TABLE foo (i integer, k charvar(250));",
                    "INSERT INTO \"foo\" VALUES(1,'hello');",
                    "INSERT INTO \"foo\" VALUES(2,'world');",
                    "COMMIT;",
                ],
            )

    @skipIf(sys.version_info < (3, 7), "Test backup() on 3.7+")
    async def test_backup_aiosqlite(self):
        def progress(a, b, c):
            print(a, b, c)

        async with aiosqlite.connect(":memory:") as db1, aiosqlite.connect(
            ":memory:"
        ) as db2:
            await db1.execute("create table foo (i integer, k charvar(250))")
            await db1.executemany(
                "insert into foo values (?, ?)", [(1, "hello"), (2, "world")]
            )
            await db1.commit()

            with self.assertRaisesRegex(OperationalError, "no such table: foo"):
                await db2.execute("select * from foo")

            await db1.backup(db2, progress=progress)

            async with db2.execute("select * from foo") as cursor:
                rows = await cursor.fetchall()
                self.assertEqual(rows, [(1, "hello"), (2, "world")])

    @skipIf(sys.version_info < (3, 7), "Test backup() on 3.7+")
    async def test_backup_sqlite(self):
        async with aiosqlite.connect(":memory:") as db1:
            with sqlite3.connect(":memory:") as db2:
                await db1.execute("create table foo (i integer, k charvar(250))")
                await db1.executemany(
                    "insert into foo values (?, ?)", [(1, "hello"), (2, "world")]
                )
                await db1.commit()

                with self.assertRaisesRegex(OperationalError, "no such table: foo"):
                    db2.execute("select * from foo")

                await db1.backup(db2)

                cursor = db2.execute("select * from foo")
                rows = cursor.fetchall()
                self.assertEqual(rows, [(1, "hello"), (2, "world")])

    @skipUnless(sys.version_info < (3, 7), "Test short circuit fail on Py 3.6")
    async def test_backup_py36(self):
        async with aiosqlite.connect(":memory:") as db1, aiosqlite.connect(
            ":memory:"
        ) as db2:
            with self.assertRaisesRegex(RuntimeError, "backup().+3.7"):
                await db1.backup(db2)
