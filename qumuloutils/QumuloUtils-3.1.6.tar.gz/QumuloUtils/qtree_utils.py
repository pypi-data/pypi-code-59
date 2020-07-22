# Copyright (c) 2019 Qumulo, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
# -----------------------------------------------------------------------------
# QTree.py
#
# QTree is a multi-processing library to "walk the file system tree" of a Qumulo
# cluster. Even though Qumulo talks about "no tree walks", there are times that
# a customer needs to walk through the entire (or directory) file system.
#
# In honor of the intention of Qumulo, this library will only walk through the
# file system ONCE if a snapshot is set as one of the arguments. Every subsequent
# "walk" of the file system will instead use the differential capability of the
# Qumulo snapshot API. This will provide us with the list of changes within the
# file system between any two given snapshots.

# Import python libraries

import time
import datetime
import functools
import multiprocessing as mp
import multiprocessing.queues as mpq
import signal
from queue import Empty, Full

DEFAULT_POLLING_TIMEOUT = 0.5

# The following are useful subroutines that fall outside of the class methodology.
# They are placed here so that it is easy to find them versus searching through this
# entire file and trying to determine what are methods and what are subroutines.

# This subroutine is the default handler for intercepting a signal. It only
# really sets the shutdown_event flag to let everyone know to terminate
# gracefully

def default_term_handler(signal_object, exception_class, signal_num, current_stack_frame):
    signal_object.terminate_called += 1
    signal_object.terminate_event.set()
    if signal_object.terminate_called >= signal_object.MAX_TERMINATE_CALLED:
        raise exception_class()

def default_int_handler(signal_object, exception_class, signal_num, current_stack_frame):
    signal_object.terminate_called += 1
    signal_object.terminate_event.set()
    if signal_object.ctrlc_event is not None:
        signal_object.ctrlc_event.set()
    if signal_object.terminate_called >= signal_object.MAX_TERMINATE_CALLED:
        raise exception_class()

# The following two subroutines are to initialize signal handling

def init_signal(signal_num, signal_object, exception_class, handler):
    handler = functools.partial(handler, signal_object, exception_class)
    signal.signal(signal_num, handler)
    signal.siginterrupt(signal_num, False)

def init_signals(terminate_event, ctrlc_event, int_handler, term_handler):
    signal_object = SignalObject(terminate_event, ctrlc_event)
    init_signal(signal.SIGINT, signal_object, KeyboardInterrupt, int_handler)
    init_signal(signal.SIGTERM, signal_object, TerminateInterrupt, term_handler)
    return signal_object

# Useful function to calculate how long to sleep

def _sleep_secs(max_sleep, end_time=999999999999999.9):
    return max(0.0, min(end_time - time.time(), max_sleep))

# The following class allows us to build a counter for a value that
# works with multiprocessing

class Counter(object):
    def __init__(self, initval=0):
        self.val = mp.Value('i', initval)
        self.lock = mp.Lock()

    def increment(self, count=None):
        with self.lock:
            if count is not None:
                self.val.value += count
            else:
                self.val.value += 1

    def decrement(self):
        with self.lock:
            self.val.value -= 1

    def value(self):
        with self.lock:
            return self.val.value

# Track some statistics for QTree... It is far easier to deposit these within their own class
# so that we can deal with them all in one place. And it gives us the capability of expanding with
# more counters in the future

class Statistics:

    def __init__(self):
        self.queued = Counter()
        self.dequeued = Counter()
        self.num_files = None
        self.num_dirs = None
        self.add_file = Counter()
        self.add_dir = Counter()
        self.modify_file = Counter()
        self.modify_dir = Counter()
        self.delete_file = Counter()
        self.delete_dir = Counter()
        self.requested_workers = Counter()
        self.alive_workers = Counter()
        self.no_cback_func = Counter()
        self.start_time = time.time()
        self.end_time = None

    # Get the summary information so that we can print it

    def summary(self):

        # Calculate all of the operations since the last call

        return self.__calc_summary()

    # Get detailed information for debugging

    def detailed(self):

        return self.__calc_detailed()

    # Calculate how many operations per second for the summaried events

    def __calc_summary(self):

        seconds = self.__calc_interval()
        dequeued_per = self.dequeued.value() / seconds
        add_file_per = self.add_file.value() / seconds
        add_dir_per = self.add_dir.value() / seconds

        summary = "Queued {0:,}, Dequeued {1:,} ({2:.2f}/sec), Files {3:,} ({4:.2f}/sec), Dirs {5:,} " \
                  "({6:.2f}/sec)".format (
                    self.queued.value(), self.dequeued.value(), dequeued_per,
                    self.add_file.value(), add_file_per, self.add_dir.value(), add_dir_per)
        return summary

    # Calculate how many operations per second for the detailed events

    def __calc_detailed(self):

        seconds = self.__calc_interval()
        date_started = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(self.start_time))
        date_ended = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(self.end_time))
        date_delta = datetime.timedelta(seconds=seconds)
        dequeued_per = self.dequeued.value() / seconds
        add_file_per = self.add_dir.value() / seconds
        add_dir_per = self.add_file.value() / seconds
        modify_file_per = self.modify_file.value() / seconds
        modify_dir_per = self.modify_dir.value() / seconds
        delete_file_per = self.delete_file.value() / seconds
        delete_dir_per = self.delete_dir.value() / seconds

        detailed = "Time Started: {0}, Time Ended: {1}, Elapsed: {2}\n".format(
            date_started, date_ended, date_delta)
        detailed = detailed + "Files in cluster {0:,}, Directories in cluster {1:,}\n".format (
            self.num_files.value(), self.num_dirs.value())
        detailed = detailed + "Files added: {0:,}, Directories added: {1:,}".format (
                self.add_file.value(), self.add_dir.value())
        return detailed

    # Calculate how many seconds have elapsed since the last call

    def __calc_interval(self):
        self.end_time = time.time()
        return self.end_time - self.start_time

# MPQueue - A class to handle queues within a multiprocessing system. The
# problem with JoinableQueue is that it depends upon a different version of
# context that could cause a problem during debugging with Python3.

class MPQueue(mpq.JoinableQueue):

    def __init__(self, *args, **kwargs):
        ctx = mp.get_context()
        super().__init__(*args, **kwargs, ctx=ctx)

    # This version of a queue get routine just returns a True/False versus
    # propogating an exception.

    def safe_get(self, timeout=DEFAULT_POLLING_TIMEOUT):
        try:
            if timeout is None:
                return self.get(block=False)
            else:
                return self.get(block=True, timeout=timeout)
        except Empty:
            return None

    # This version of a queue put routine just returns a True/False versus
    # propogating an exception.

    def safe_put(self, item, timeout=DEFAULT_POLLING_TIMEOUT):
        try:
            self.put(item, block=False, timeout=timeout)
            return True
        except Full:
            return False

    # Drain the queue of all of the items. This is used when the main program
    # wants to terminate. You should never try to close a queue without first
    # draining it.

    def drain(self):
        item = self.safe_get()
        while item:
            yield item
            self.task_done()
            item = self.safe_get()

    # Close the queue... In order to avoid the problem of hanging because the
    # queue has items in it, this routine will drain the queue before closing
    # it.

    def safe_close(self):
        num_left = sum(1 for __ in self.drain())
        try:
            self.close()
        except Exception as exc:
            pass
        finally:
            return num_left

# Safely handle Signals... There is not a good mechanism for handling terminate
# and keyboard interrupt (ctrl-C) signals within spawned processes. We will do
# that with this class and its supporting routines.

class TerminateInterrupt(BaseException):
    pass

class SignalObject:
    MAX_TERMINATE_CALLED = 3

    def __init__(self, terminate_event, ctrlc_event):
        self.terminate_called = 0
        self.terminate_event = terminate_event
        self.ctrlc_event = ctrlc_event

