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
import os
import time
import multiprocessing as mp
import threading
import logging
import logging.config
import logging.handlers
from queue import Empty

# Import Qumulo Libraries

from QumuloUtils.qcluster import QCluster
from QumuloUtils.qtree_workers import QueueWorker
from QumuloUtils.qtree_utils import (
    MPQueue, _sleep_secs, Counter, init_signals, default_int_handler, default_term_handler, Statistics,
)

# Build a callback class... A callback is used when you want further
# processing down to a particular item. This is a "master" class that we
# expect that a user will overload in order to provide "next step" processing.

class QTreeCallback:

    def __init__(self, name, logger, qcluster, callback_info=None):

        self.procname = name
        self.logger = logger
        self.qcluster = qcluster
        self.cback_info = callback_info

        # The normal logger will not work in a spawned process. So, we fixed this
        # by creating a multiprocessing logger that works as a separate process.
        # The normal logger calls to "debug, error, warning, and info" work by placing
        # a message into a queue for the process to dump.

        self.logger.debug("Init done for QTree Callback.")

    # Create a file document

    def create_file(self, entry):

        self.logger.debug("create_file not implemented in callback.")

    # Delete a file entry

    def delete_file(self, entry):

        self.logger.debug("delete_file not implemented in callback.")

    # Modify a file entry

    def modify_file(self, entry):

        self.logger.debug("modify_file not implemented in callback.")

    # Create a directory entry

    def create_dir(self, entry):

        self.logger.debug("create_dir not implemented in callback.")

    # Delete a directory entry

    def delete_dir(self, entry):

        self.logger.debug("delete_dir not implemented in callback.")

    # Modify a directory entry

    def modify_dir(self, entry):

        self.logger.debug("modify_dir not implemented in callback.")

    # The program is done... Start the tear down (if needed)

    def tear_down(self):
        pass

#
# QTree Class
#
# This class inherits the QCluster class from QumuloUtils in order to work with a
# Qumulo Cluster API.
#
# This class will perform either a full or partial scan of a Qumulo filesystem using
# the API in order to find certain user data patterns. It will optionally call a routine
# (callback provided by customer) that will provide additional individual file processing.

class QTree(QCluster):

    STOP_WAIT_SECS = 3.0
    int_handler = staticmethod(default_int_handler)
    term_handler = staticmethod(default_term_handler)

    def __init__(self, progname, qhost, qlogin="admin", qpasswd="admin", qport=8000, loglevel=None,
                 start_path=None, num_threads=None, callback=None, callback_info=None,
                 snapshot_name=None, statistics=None):

        super(QTree, self).__init__(qhost=qhost, qlogin=qlogin, qpasswd=qpasswd,
                                    qport=qport, logger=None)

        self._log_finish = False
        self.progname = progname
        self.start_path = None
        self.statistics = statistics
        self.snapshot_name = snapshot_name
        self.last_snapshot = None
        self.qhost = qhost
        self.qlogin = qlogin
        self.qpasswd = qpasswd
        self.qport = qport
        self.loglevel = loglevel
        self.callback_info = callback_info
        self.procs = []
        self.terminate_event = mp.Event()
        self.ctrlc_event = mp.Event()
        self.dir_q = MPQueue()
        self.log_q = mp.Queue()
        self.stats = Statistics()
        self.ips = None
        self.logger = None
        self.log_thread = None
        self.inc_scan = False
        self.inc_no_files = False

        # Did they pass in a callback routine. If not, then use our default
        # so that we have debugging output

        if callback is None:
            self.callback = QTreeCallback
        else:
            self.callback = callback

        # Make sure the start path ends with a "/"

        start_len = len(start_path)

        if start_path[start_len - 1] != "/":
            self.start_path = start_path + "/"
        else:
            self.start_path = start_path

        # Set the maximum number of threads...
        
        if num_threads is None:
            self.num_threads = 1
        else:
            self.num_threads = num_threads

        # Setup the signal handler so that we can terminate when ctrl-C
        # or a kill is received.

        init_signals(self.terminate_event, self.ctrlc_event, self.int_handler, self.term_handler)

        # Start the logger process...

        self.create_logger()
        self.start_logger()
        self.logger.debug("%s - Cluster %s will start at path %s", "QTree", qhost, self.start_path)

    # Start the logger thread

    def start_logger(self):

        self.log_thread = threading.Thread(target=self.__logging_thread, args=(self.log_q,))
        self.log_thread.start()

    # Create the logger and logger filters

    def create_logger(self):

        log_dir = self.build_results_dir()
        dict = self.build_logging_dict(log_dir)
        logging.config.dictConfig(dict)

        # Change the default log level on the root of the logger

        self.logger = logging.getLogger()
        self.logger.setLevel(self.loglevel)

    # Build the logging dictionary. We are doing this in a method as they might want to override it
    # with a different method

    def build_logging_dict(self, log_dir):

        # Build the filter and handler dictionary... Change THIS if you want to setup different filters

        logdict = {
            'version': 1,
            'formatters': {
                'detailed': {
                    'class': 'logging.Formatter',
                    'format': '%(asctime)s %(funcName)-10s %(levelname)-8s %(processName)-10s %(message)s'
                },
                'console': {
                    'class': 'logging.Formatter',
                    'format': '%(message)s'
                },
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'INFO',
                    'formatter': 'console',
                },
                'file': {
                    'class': 'logging.FileHandler',
                    'filename': log_dir + '/all.log',
                    'mode': 'w',
                    'formatter': 'detailed',
                },
                'errors': {
                    'class': 'logging.FileHandler',
                    'filename': log_dir + '/error.log',
                    'mode': 'w',
                    'level': 'ERROR',
                    'formatter': 'detailed',
                },
                'debug': {
                    'class': 'logging.FileHandler',
                    'filename': log_dir + '/debug.log',
                    'mode': 'w',
                    'level': 'DEBUG',
                    'formatter': 'detailed',
                },
            },
            'root': {
                'handlers': ['console', 'file', 'errors', 'debug'],
                'propagate': False,
            },
        }

        return logdict

    # Build logging results directory

    def build_results_dir(self):
        # For the purposes of simplicity, we will store the log files in a subdirectory of where this
        # program executes. If you want to change it, do it here.

        base_dir = "."

        # Understand the type of cluster. This will be used as a basis to create a directory
        # structure in order to store the log files. In this way, we can have a different
        # directory structure for logs based upon the type of cluster we are working on.

        (model, version, clustername, node_count) = self.cluster_info()

        # Get version... It is the third item in the array (2 starting from 0)

        info = version.rsplit(' ')
        versinfo = info[2]

        # Get the date and time for format it

        dateinfo = time.strftime("%Y%m%d%H%M%S")

        # Build the results directory such:
        #
        # resultsdir / model / version / datetime

        resultsdir = base_dir + "/" + model + "/" + versinfo + "/" + dateinfo

        # We have to make sure that the directory is created before
        # we can use it. The assumption is that the directory does
        # not exist.

        try:
            os.makedirs(resultsdir, mode=0o755)
        except Exception as excpt:
            self.logger.error('Error on makedirs = %s', excpt)
            sys.exit(1)

        return resultsdir

    # Routine to start all of the worker processes

    def start_workers(self):

        # Create workers based upon number of threads

        self.logger.debug("Starting QueueWorkers.")

        # Get a list of all the IP's for the cluster. In order to get a fair distribution
        # for all of the threads (processes) across the nodes, we cannot trust that the
        # users have given us a cluster name that is round-robin'd in the DNS.

        self.ips = self.cluster_ips()

        cur_ip = 0

        for indx in range(self.num_threads):
            procname = "Worker-" + str(indx +1)
            proc = QueueWorker(procname, self.terminate_event, self.log_q,
                               self.dir_q, self.stats, callback=self.callback,
                               call_info=self.callback_info, host=self.ips[cur_ip],
                               login=self.qlogin, passwd=self.qpasswd, port=self.qport)
            self.procs.append(proc)
            proc.start()

            # Make sure we select the next IP

            cur_ip += 1
            if cur_ip == len(self.ips):
                cur_ip = 0

    # Abort the qtree walk... This can only be called by a routine outside of the class
    # since, by default, we don't know where we are in the processing.
    #
    # This is usually called only when a Ctrl-C is intercepted.

    def abort_operation(self):

        self.logger.debug("Abort operation in progress.")

        # Get rid of any snapshot since the process has aborted and we will probably
        # have to start over...

        if self.last_snapshot is not None:
            self.remove_snapshot(self.last_snapshot)
            self.last_snapshot = None

    # This is the main routine for the class. Somebody using the class would instantiate it,
    # then execute the "run" (this routine) and finally would do a TearDown before they
    # are ready to abandon the class...

    def run(self):

        # Do we have a snapshot name? If so, then determine if a snapshot exists and we
        # can use the incremental feature versus doing a complete walk

        if self.snapshot_name is not None:
            snap_list = self.find_snapshot(self.snapshot_name)
            if snap_list is not None:
                self._inc_scan()
            else:
                self._full_scan()
        else:
            self._full_scan()

    # Routine to wait for the queue to empty. We need this so that the children have time
    # to process the queue entries
    #
    # You will notice that there are two events that seem similar (terminate and shutdown). Terminate is when
    # we want to tell ALL of the workers to go away. If one of the workers sets the terminate event, then
    # something disasterous has occurred and all of the workers (and ourselves) should go away.
    #
    # Shutdown is a per worker event and that is when they are telling us that they no longer have any
    # work and are going away normally

    def _wait_for_complete(self):

        # Continue to wait

        wait_count = 0

        while True:

            # If this was a incremental scan and there was no work, then just immediately exit...

            if self.inc_scan and self.inc_no_files:
                break

            # If all of the workers are not alive and the shutdown_event was not fired,
            # then something is wrong. Abort!

            if self.terminate_event.is_set():

                # Determine if we really got a worker that aborted or if the operation hit ctrl-c to manually
                # terminate...

                if self.ctrlc_event.is_set():
                    self.logger.error("Operator manually aborted. Terminating all operations!")
                else:
                    self.logger.error("A worker aborted abnormally. Terminating operations!")

                self.abort_operation()
                sys.exit(1)

            if not self._workers_alive():
                wait_count += 1
                if (wait_count % 10) == 0: # show status every ~10 seconds
                    if self.statistics:
                        summary_info = self.stats.summary()
                        print(summary_info)
                time.sleep(1)
            else:
                break

        # All is done... If they want info, then give them a detailed list

        if self.statistics and (not self.inc_scan and not self.inc_no_files):
            detailed_info = self.stats.detailed()
            print(detailed_info)

        self.logger.debug("Everything is completed. Exiting.")

    # Logging thread... This thread handles all of the logging for every process. Since logging is thread
    # safe, but NOT multiprocessing safe, we have to use a queue to send all of the messages that we want
    # logged.

    def __logging_thread(self, log_q):
        while not self._log_finish:
            try:
                record = log_q.get(block=False, timeout=1.0)
                self.logger.handle(record)
            except Empty:
                pass

    # Called by the context... Just return ourselves

    def __enter__(self):
        return self

    # This is called when the process wants to terminate.

    def __exit__(self, exc_type, exc_val, exc_tb):

        # Terminate all of the processes

        self._stop_queues()
        self._stop_procs()

        # Terminate the log thread last

        self._log_finish = True
        self.log_thread.join()

        return 0

    # Routine to stop all of the worker processes

    def _stop_procs(self):
        self.terminate_event.set()
        end_time = time.time() + self.STOP_WAIT_SECS
        num_terminated = 0
        num_failed = 0

        # Wait for STOP_WAIT_SECS for all processes to complete

        for proc in self.procs:
            join_secs = _sleep_secs(self.STOP_WAIT_SECS, end_time)
            proc.join(join_secs)

        # Clear the procs list and TERMINATE any proces that have not yet exited

        still_running = []
        while self.procs:
            proc = self.procs.pop()
            if proc.is_alive():
                if proc.terminate():
                    num_terminated += 1
                else:
                    still_running.append(proc)
            else:
                exitcode = proc.exitcode
                if exitcode:
                    self.logger.error(f"QTree process {proc.name} ended with exitcode {exitcode}")
                    num_failed += 1
                else:
                    self.logger.debug(f"QTree process {proc.name} stopped successfully")

        self.procs = still_running
        return num_failed, num_terminated

    # Routine to drain and close the queues

    def _stop_queues(self):

        # Drain the queue

        num_items_left = self.dir_q.safe_close()
        return num_items_left

    # Add a new entry to the processing queue

    def _add_to_q(self, operation, fsid):

        self.dir_q.safe_put({"operation": operation, "id": fsid})
        self.stats.queued.increment()

    # Routine to do a incremental scan. This compares two snapshots and gets a list
    # of created, modified, and deleted files.

    def _inc_scan(self):

        self.logger.info("Initiating an incremental scan using snapshot %s.", self.snapshot_name)

        # We have to create a second snapshot to compare to...

        self.last_snapshot = self.create_snapshot(self.snapshot_name, self.start_path)

        # How we handle the completion of incremental scans is different than what we do for a full scan...
        # Incremental scanning controls the placement of modifications on the queue. Because of that,
        # we know when there is no more content and we can terminate immediately.

        self.inc_scan = True
        self.inc_no_files = False

        # Go and get the list of entries to compare work against...

        next_page = "first"

        while next_page is not None:
            try:
                (created, modified, deleted, next_page) = self.compare_snapshot(self.snapshot_name)
            except Exception:

                # Get rid of the snapshot that we just created since our comparison failed...
                # If we don't get rid of it, then we cannot accurately compare against the time
                # period in question.

                self.remove_snapshot(self.last_snapshot)
                return

            created_len = len(created)
            modified_len = len(modified)
            deleted_len = len(deleted)
            total_modified = created_len + modified_len + deleted_len

            # Print out how many entries have been changed

            if self.statistics:
                inc_info = "{0} created, {1} modified, {2} deleted".format(created_len, modified_len, deleted_len)
                print(inc_info)

            # There may be no incremental data... If true, then set the flag for later
            # when we are in the completion mode

            if total_modified == 0 and next_page is None:
                self.inc_no_files = True
                break

            # Cycle through the created entries and add them to the processing queue

            for ent in created:
                self._verify_entry_type("add", ent)

            # Cycle through the modified entries and add them to the processing queue

            for ent in modified:
                self._verify_entry_type("modify", ent)

            # Cycle through the deleted entries and add them to the processing queue

            for ent in deleted:
                self._verify_entry_type("delete", ent)

        # Finally, delete all of the old snapshots except for the last one...

        self.remove_old_snapshot(self.snapshot_name)
        self.last_snapshot = None

    # Routine to do a full scan from a "start_path"

    def _full_scan(self):

        msg_str = "Initiating a full scan"
        if self.snapshot_name is not None:
            msg_str = msg_str + ", and creating snapshot {} to track incremental changes.".format(self.snapshot_name)
        else:
            msg_str = msg_str + "."

        self.logger.info(msg_str)

        # If they defined a snapshot_name, then we should take one at the beginning. This will
        # be used during the next incremental for comparison purposes.

        if self.snapshot_name is not None:
            self.last_snapshot = self.create_snapshot(self.snapshot_name, self.start_path)

        # Read the aggregates from the start_path...

        root = self.connection.fs.read_dir_aggregates(path=self.start_path, max_entries=0)

        # Add the directors and files to statistics. Print out the values if
        # summary is set

        num_dirs = int(root["total_directories"])
        num_files = int(root["total_files"])

        self.stats.num_files = Counter(num_files)
        self.stats.num_dirs = Counter(num_dirs)

        if self.statistics:
            print("Directories to scan:%20s" % "{:,}".format(num_dirs))
            print("Files to scan:%26s" % "{:,}".format(num_files))

        # Add this directory to a queue to process

        self._add_to_q("add_dir", root['id'])

    # Verify entry type and add it to the processing queue

    def _verify_entry_type(self, operation, entry):
        leng = len(entry)

        if entry[leng - 1] == "/":
            self._add_to_q(operation + "_dir", entry)
        else:
            self._add_to_q(operation + "_file", entry)

    # Are all of the worker processes alive or not?

    def _workers_alive(self):

        # Look at every worker and see if they are alive. This routine returns either a false
        # or a true based upon the status of ANY of the workers

        current_status = True

        for proc in self.procs:
            if not proc.is_alive():
                self.procs.remove(proc)

        if len(self.procs) > 0:
            current_status = False

        return current_status
