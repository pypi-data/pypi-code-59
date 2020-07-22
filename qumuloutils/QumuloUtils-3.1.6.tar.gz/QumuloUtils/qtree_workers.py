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

import sys
import logging
import logging.config
import logging.handlers
import multiprocessing as mp

# Import Qumulo Libraries

from QumuloUtils.qcluster import QCluster
from QumuloUtils.qtree_utils import (
    Statistics, default_int_handler, default_term_handler, init_signals)

# This is the maximum time we will wait for something to come in on our worker queues
# If it doesn't come in by then, then terminate our process

MAX_QUEUE_WAIT_TIME = 0.5
MAX_ITERATIONS = 60

# This class will handle the message for the Queue being full

class QueueIsFull(Exception):

    def __init__(self, data="The Queue is full!"):
        self.data = data
        super().__init__(self.data)

    def __str__(self):
        return repr(self.data)

# This class will handle the message for a termination request

class TerminateRequest(Exception):

    def __init__(self, data="Termination was requested!"):
        self.data = data
        super().__init__(self.data)

    def __str__(self):
        return repr(self.data)

# This class will handle all of the work for processes 2 thru N
# In the multiprocessing model (versus the Threading model), this is
# not supposed to be a class. I find that handling this as a class is
# far easier to debug as I can separate the functionality. However,
# this class needs to be instantiated by a function (which is the
# starting point for each process.

class WorkerProc(mp.Process):
    MAX_TERMINATE_CALLED = 3
    int_handler = staticmethod(default_int_handler)
    term_handler = staticmethod(default_term_handler)

    def __init__(self, name, terminate_event, log_q, dir_q, stats, **kwargs):

        super(WorkerProc, self).__init__(name=name)
        self.procname = name
        self.terminate_event = terminate_event
        self.log_q = log_q
        self.dir_q = dir_q
        self.stats = stats
        self.logger = None

    # Register the SIGINT and SIGTERM signals

    def init_signals(self):
        self.logger.debug("Entering init_signals in Worker Process.")
        signal_object = init_signals(self.terminate_event, None, self.int_handler, self.term_handler)
        return signal_object

    def startup(self):

        # Create connection to log handler

        qhandler = logging.handlers.QueueHandler(self.log_q)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(qhandler)
        self.logger.debug("Entering generic startup in Worker Process.")
        pass

    def shutdown(self):
        self.logger.debug("Entering generic shutdown in Worker Process.")
        self.log_q.close()
        pass

    def self_destruct(self):
        if self.logger is not None:
            self.logger.debug("Entering generic terminate in Worker Process.")
        self.terminate_event.set()
        self.dir_q.safe_close()
        pass

    def abort_all(self):
        self.self_destruct()
        sys.exit(0)

    def main_loop(self):
        self.logger.debug("Entering main_loop in Worker Process.")
        while not self.terminate_event.is_set():
            self.main_func()

    def main_func(self):
        self.logger.debug("Entering dummy main_func in Worker Process.")
        raise NotImplementedError(f"{self.__class__.__name__}.main_func is not implemented")

    # This is the main function loop for a process... It is called from the wrapper and implements all of the
    # code for a process.

    def run(self):
        self.startup()
        self.init_signals()
        try:
            self.main_loop()
            self.logger.debug("Normal Shutdown")
            pass
        except QueueIsFull as exc:
            self.logger.error(exc)
            self.terminate()
        except SystemExit as exc:
            pass
        except BaseException as exc:
            self.self_destruct()
        finally:
            self.shutdown()

# QueueWorker - Derivative of WorkerProcess. This class is built around the idea of
# how to handle messages for the main workers.

class QueueWorker(WorkerProc):

    # There are only SMALL differences from the base class __init__ method
    # Call the base class __init__ and then add our stuff

    def __init__(self, name, terminate_event, log_q, dir_q, stats, **kwargs):

        super(QueueWorker, self).__init__(name, terminate_event, log_q, dir_q, stats, **kwargs)
        self.host = kwargs.get("host", None)
        self.login = kwargs.get("login", None)
        self.passwd = kwargs.get("passwd", None)
        self.port = kwargs.get("port", None)
        self.callback = kwargs.get("callback", None)
        self.call_info = kwargs.get("call_info", None)
        self.qcluster = None
        self._callback = None

    # Register the callback routine

    def register_callback(self):

        # The callback needs to be instantiated per thread. So, it is done here.

        if self.callback is not None:
            if self.call_info is not None:
                self._callback = self.callback(self.procname, self.logger, self.qcluster, self.call_info)
            else:
                self._callback = self.callback(self.procname, self.logger, self.qcluster, callback_info=None)

    # Need a new startup routine in order to make sure that we register
    # the callback routines...

    def startup(self):

        # We have to call the generic startup since this is where the logger is setup.

        super(QueueWorker, self).startup()
        self.logger.debug("Entering startup in QueueWorker Process.")

        # This is a forked process and nothing survived. We need to re-instantiate
        # everything. Start by making a connection to the cluster.

        try:
            self.qcluster = QCluster(self.host, self.login, self.passwd, self.port, self.logger)
        except BaseException as exc:
            self.logger.error("Could not connect to cluster, error was %s.", exc)
            self.abort_all()

        # Register the callback routine

        self.register_callback()
        pass

    # Loop through getting the data from the queue. But, if we have nothing, then shutdown

    def main_loop(self):
        self.logger.debug("Entering main_loop in QueueWorker process.")

        # Call the main_func N number of times... This will keep us from getting stuck
        # in this function when there is absolutely no work to do.

        num_iterations = 0

        while not self.terminate_event.is_set():
            while num_iterations <= MAX_ITERATIONS:
                if not self.main_func():
                    num_iterations += 1
                else:
                    num_iterations = 0

            return

    # Here is where we get the data from the queue and process it. If we don't get data within
    # a given period of time, then exit and shutdown.

    def main_func(self):

        entry = self.dir_q.safe_get(timeout=MAX_QUEUE_WAIT_TIME)
        if entry is not None:
            self.stats.queued.decrement()

            # Determine what they want to do and call that routine...

            op_type = entry["operation"]
            func = self._get_method(self, op_type)
            if func is not None:
                try:
                    func(self._callback, entry["id"])
                except BaseException as exc:

                    # We have an unknown exception... Set the task_done on the queue
                    # and abort

                    self.logger.error("Exception during %s operation. Error is %s.", op_type, exc)
                    self.dir_q.task_done()
                    self.abort_all()
            else:
                self.stats.no_cback_func.increment()
                self.logger.debug("%s operation is not defined in worker.", entry["operation"])

            self.stats.dequeued.increment()
            self.dir_q.task_done()
            return True
        else:
            return False

    # This is called only from the incremental scan... The normal "add_file" is handled when
    # parsing through a directory.

    def add_file(self, callback, path):

        # Get the file entry....

        qconn = self.qcluster.get_connection()

        try:
            ent = qconn.fs.get_file_attr(path=path)
        except Exception as excpt:
            self.logger.error("Cannot get file info for path %s, error is %s.", path, excpt)
            raise

        if ent["type"] == "FS_FILE_TYPE_FILE":

            # Make sure we count this operation

            self.stats.add_file.increment()

            if callback is not None:
                if self._has_method(callback, 'create_file'):
                    callback.create_file({"process-entry": ent})
                else:
                    self.logger.error("No valid CreateFile method in callback")

    # List each entry in the directory

    def add_dir(self, callback, fsid):

        # Get the directory entries.. If we have a "next page", then retrieve that instead.

        qconn = self.qcluster.get_connection()

        next_page = "first"

        while next_page is not None:

            # Make sure we count this operation
            # We only need to count it here since EVERY new directory comes through this code
            # This is NOT true for adding a file as they can be embedded within a directory
            # and need to be counted when found...

            self.stats.add_dir.increment()

            # These file operations can take a VERY long time. Make sure that the terminate
            # didn't get set..

            if self.terminate_event.is_set():
                raise TerminateRequest()

            # Either read the directory for the first time or process a "next" page

            if next_page == "first":
                dir_entry = qconn.fs.read_directory(id_=fsid, page_size=2000)
            else:
                dir_entry = qconn.request("GET", next_page)

            if dir_entry['paging']['next'] != "":
                next_page = dir_entry['paging']['next']
            else:
                next_page = None

            # Process each entry returned. If a file, then process through a "callback routine" if
            # it exists. If a directory, process it through a "callback routine" and then put it on
            # the queue for further processing by another thread.

            for ent in dir_entry["files"]:

                # Again, these operations can take a long time... Check that the terminate
                # is not set before we do any of them

                if self.terminate_event.is_set():
                    raise TerminateRequest()

                # If this is a file, then process it...

                if ent["type"] == "FS_FILE_TYPE_FILE":

                    self.stats.add_file.increment()

                    if callback is not None:
                        if self._has_method(callback, 'create_file'):
                            callback.create_file({"process-entry": ent})
                        else:
                            self.logger.error("No valid CreateFile method in callback")

                # If a directory, then we need to do some further processing

                if ent["type"] == "FS_FILE_TYPE_DIRECTORY" and int(ent["child_count"]) > 0:

                    # Before we put it in the queue for processing by another thread, we
                    # will add the directory entry. In order to do that, we will need to
                    # get the directory aggregates so that we have an accurate file and subdir
                    # count

                    # Now put it on the queue for processing by another thread

                    self._add_to_q({"operation": "add_dir", "id": ent["id"]})

                    # Call the callback object to process the directory entry (if it exists)

                    if callback is not None:
                        if self._has_method(callback, 'create_dir'):
                            callback.create_dir({"process-entry": ent})
                        else:
                            self.logger.error("No valid CreateDir method in callback")
                elif ent["type"] == "FS_FILE_TYPE_DIRECTORY" and int(ent["child_count"]) == 0:

                    # We need to count zero length directories only so that we can say we have
                    # walked them

                    self.stats.add_dir.increment()

    # This is called only from the incremental scan... Full scans look like everything is a new
    # file or directory

    def modify_file(self, callback, path):

        # Get the file entry....

        qconn = self.qcluster.get_connection()

        try:
            ent = qconn.fs.get_file_attr(path=path)
        except Exception as excpt:
            self.logger.error("Cannot get file info for path %s, error is %s.", path, excpt)
            raise

        if ent["type"] != "FS_FILE_TYPE_FILE":
            self.logger.error("%s is not a file during a ModifyFile operation.", path)
            return

        # Make sure we count the operation

        self.stats.modify_file.increment()

        # If there is a callback routine, then execute it

        if callback is not None:
            if self._has_method(callback, 'modify_file'):
                callback.modify_file({"process-entry": ent})
            else:
                self.logger.error("No valid ModifyFile method in callback")

    # This is called only from the incremental scan... Full scans look like everything is a new
    # file or directory

    def modify_dir(self, callback, path):

        # Get only the one directory entry..

        qconn = self.qcluster.get_connection()

        # Get the attributes of the directory

        try:
            ent = qconn.fs.get_file_attr(path=path)
        except Exception as excpt:
            self.logger.error("Cannot get directory info for path %s, error is %s.", path, excpt)
            raise

        # Make sure that it is a directory. If not, then print an error and move on...
        # In the future, we might have to raise an exception. But, seeing as this
        # is a spawned worker process, I am not sure how to do that yet and make it
        # relevant... :-)

        if ent["type"] != "FS_FILE_TYPE_DIRECTORY":
            self.logger.error("%s is not a directory during a ModifyDir operation.", path)
            return

        # Make sure we count the operation

        self.stats.modify_dir.increment()

        # If there is a callback routine, then execute it

        if callback is not None:
            if self._has_method(callback, "modify_dir"):
                callback.modify_dir({"process-entry": ent})
            else:
                self.logger.error("No valid ModifyDir method in callback ")

    # This is called only from the incremental scan... Full scans look like everything is a new
    # file or directory

    def delete_file(self, callback, path):

        # Make sure we count the operation

        self.stats.delete_file.increment()

        # Because the file is actually deleted, we cannot do anything but
        # call the callback routine and let the user do some processing
        # (if they want).

        if callback is not None:
            if self._has_method(callback, 'delete_file'):
                callback.delete_file({"process-entry": path})
            else:
                self.logger.error("No valid DeleteFile method in callback")

    # This is called only from the incremental scan... Full scans look like everything is a new
    # file or directory

    def delete_dir(self, callback, path):

        # Make sure we count the operation

        self.stats.delete_dir.increment()

        # Because the directory is actually deleted, we cannot do anything but
        # call the callback routine and let the user do some processing
        # (if they want).

        if callback is not None:
            if self._has_method(callback, "delete_dir"):
                callback.delete_dir({"process-entry": path})
            else:
                self.logger.error("No valid DeleteDir method in callback ")

    # Determine if a method exists within a class. This is needed because a caller might give
    # us a callback to use. We have to determine if the method exists or not.

    def _has_method(self, qtree_oper, name):
        return callable(getattr(qtree_oper, name, None))

    # Get the address of the method and return it...

    def _get_method(self, qtree_oper, name):
        if self._has_method(qtree_oper, name):
            return getattr(qtree_oper, name, None)
        else:
            return None

    # Add a new entry to the processing queue

    def _add_to_q(self, entry):

        if not self.dir_q.safe_put(entry):
            self.logger.debug("Queue Full")
            raise QueueIsFull()
        else:
            self.stats.queued.increment()
