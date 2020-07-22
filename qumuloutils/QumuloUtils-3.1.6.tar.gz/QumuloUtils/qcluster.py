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
# QCluster.py
#
# This class contains all the code necessary to deal with a Qumulo Cluster;
# including Clearing the Cache, Getting the Cluster Type, Getting the Cluster IPs,
# and finding out if the Cluster is Rebuilding.


# Import Qumulo REST Libraries

import qumulo.lib.auth
import qumulo.lib.opts
import qumulo.lib.request as request
import qumulo.rest
from qumulo.lib.uri import UriBuilder
from qumulo.rest_client import RestClient

import logging

#
# QCluster Class
#
# This class contains all the code necessary to deal with a Qumulo Cluster;
# including finding files based upon age, file type, and/or file size.


class QCluster:

    def __init__(self, qhost, qlogin="admin", qpasswd="admin", qport=8000, logger=None):

        self.logger = logger
        self.qhost = qhost
        self.qport = int(qport)
        self.qlogin = qlogin
        self.qpasswd = qpasswd
        self.connection = None
        self.credentials = None
        self.resultsdir = None
        self.saved_files = []
        self.bucket_number = 1
        self.total_dirs = 0
        self.found_dirs = 0
        self.total_files = 0
        self.found_files = 0
        self.type_sizes = []
        self.type_counts = []
        self.first_scan = True
        self.node_info = None

        # If there was no logger passed in, then use the root logger.
        # We need a logger for the various errors or debugging

        if self.logger is None:
            self.logger = logging.getLogger()

        # Create a connection to the cluster

        try:
            self.connection = RestClient(self.qhost, self.qport)

            # Login and store credentials

            self.credentials = self.connection.login(self.qlogin, self.qpasswd)
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to login to Qumulo cluster. Error is %s', excpt)
            raise

    # Clear the cache on the cluster

    def clear_cache(self):

        # We are building this "by hand" as we don't want to have
        # the users of these scripts load the internal qumulo libraries.

        method = "POST"
        uri = str(UriBuilder(path="/v1/debug/cache/clear"))

        try:
            request.rest_request(self.connection, self.credentials, method, uri)
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Exception on clearing cache. Error is %s', excpt)

            raise

    # Get some info from the cluster for logging

    def cluster_info(self):

        # First, get the model number from the nodes. We will store the
        # node_info structure if they need it for later.

        try:
            self.node_info = self.connection.cluster.list_nodes()
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to list_nodes in cluster. Error is %s', excpt)
            raise

        # Get the number of nodes

        node_count = int(len(self.node_info))

        # Get the model number from the nodes. "There can be only one!"

        model = str(self.node_info[0]['model_number'])

        # Get the revision for the cluster

        try:
            versinfo = self.connection.version.version()
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to get version from cluster. Error is %s', excpt)

            raise

        # Get the version of software from the cluster.

        version = str(versinfo['revision_id'])

        # Get the name of the cluster

        try:
            name_info = self.connection.cluster.get_cluster_conf()
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to get name of the cluster. Error is %s', excpt)

            raise

        # Get the name of the cluster

        cluster_name = str(name_info['cluster_name'])

        return (model, version, cluster_name, node_count)

    # Get the connection for making "raw" calls

    def get_connection(self):

        return self.connection

    # Find out what IP addresses are in use by the cluster.
    # We will look at both the "management" and the floating
    # IP's. If they have floating IP's, those will always
    # be used over the "management" IP's.

    def cluster_ips(self):

        # Get the status of the network. This will return both the
        # "management" and the floating IP's. The floating IP's will
        # have an array length of 0 if there are none. So, this is easy!

        try:
            ifinfo = self.connection.network.list_interfaces()
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to get network interfaces from cluster. Error is %s',
                                  excpt)
            raise

        try:
            net_info = self.connection.network.list_network_status_v2(ifinfo[0]['id'])
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to get network information from cluster. Error is %s',
                                  excpt)
            raise

        ips = []

        for info in net_info:
            net_status = info['network_statuses']

            if len(net_status[0]['floating_addresses']) > 0:
                for floats in net_status[0]['floating_addresses']:
                    ips.append(str(floats))
            else:
                ips.append(str(net_status[0]['address']))

            # Sort the IPs and then return it

        ips.sort()

        return ips

    # Find out if the cluster is doing a rebuild. This is only allowed if
    # the benchmarker wants this (set via the configuration file). Otherwise,
    # this is an error condition.

    def cluster_rebuilding(self):

        try:
            rebuild_info = self.connection.cluster.get_restriper_status()
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to get restriper status from cluster. Error is %s',
                                  excpt)
            raise

        status = rebuild_info['status']

        if status == "NOT_RUNNING":
            return False

        return True

    # Cycle through a named set of snapshots and delete the oldest greater than the limit

    def cycle_snapshot(self, snap_list, limit=None):

        # If there is a limit, then delete all older snapshots greater than the limit

        if limit is not None:
            our_limit = 1
        else:
            our_limit = limit

        # If we don't have enough snapshots to match the limit, then move on

        if len(snap_list) <= our_limit:
            return

        # Delete all snapshots greater than the limit

        num_del = len(snap_list) - our_limit
        if num_del > 0:
            for sid in range(num_del):
                snap_id = snap_list(sid)['id']

                try:
                    self.connection.snapshot.delete_snapshot(snap_id)
                except Exception as excpt:
                    if self.logger is not None:
                        self.logger.error("Snapshot id %s was incorrectly deleted, error was %s.",
                                          snap_id, excpt)
                        raise

    # Delete a snapshot

    def remove_snapshot(self, snapid):

        try:
            self.connection.snapshot.delete_snapshot(snapid)
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error("Snapshot %d could not be deleted, error was %s", snapid, excpt)
                raise

    # Delete all of the old snapshots but one...

    def remove_old_snapshot(self, name):

        # First, get all of the snapshots that match our name

        snap_list = self.find_snapshot(name)

        # Now, delete all of them except for the last one

        for indx in range(0, len(snap_list) - 1):
            try:
                self.connection.snapshot.delete_snapshot(snap_list[indx]["id"])
            except Exception as excpt:
                if self.logger is not None:
                    self.logger.error("Snapshot %d was already deleted, error was %s.",
                                      snap_list[indx]["id"], excpt)
                    raise

    # Create a new snapshot based upon the snapshot name

    def create_snapshot(self, name, path):

        try:
            value = self.connection.snapshot.create_snapshot(name=name, path=path)
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to create a snapshot. Error is %s', excpt)
                raise

        return value["id"]

    # Return the list of entries from two compared snapshots

    def _return_snap_info(self, snap_entries):

        created_list = []
        modified_list = []
        deleted_list = []
        next_page = snap_entries["paging"]["next"]


        # Iterate through the list and get all of the created, modified, and deleted

        if len(snap_entries["entries"]) > 0:
            (clist, mlist, dlist) = self._return_snap_diffs(snap_entries["entries"])

            for indx in enumerate(clist):
                created_list.append(indx[1])

            for indx in enumerate(mlist):
                modified_list.append(indx[1])

            for indx in enumerate(dlist):
                deleted_list.append(indx[1])

        return (created_list, modified_list, deleted_list, next_page)

    # Get the next list of changes from the two snapshots. This is called if a previous
    # CompareSnapshot routine returned a "next_page".

    def get_next_from_snapshot(self, next_page):

        # Get the next page of changes

        if next_page is not None:
            try:
                snap_entries = self.connection.request("GET", next_page)
            except Exception as excpt:
                if self.logger is not None:
                    self.logger.debug("Error %s retrieving the next page of snapshot changes.",
                                      excpt)
                    raise

            # Iterate through the list and get all of the created, modified, and deleted

            (created_list, modified_list, deleted_list, next_page) = \
                self._return_snap_info(snap_entries["entries"])

        return (created_list, modified_list, deleted_list, next_page)

    # Compare two snapshots by using a snapshot list. This routine is called if they
    # previously used the routine FindSnapshot and got a snapshot list. You should never
    # pass in a list of all of the snapshots (regardless of name). That won't work since this
    # routine will pick the last two snapshots to compare them and, if they are not the same
    # name, then it will fail.

    def compare_snapshot_list(self, snap_list):

        # Make sure the snapshot list is not empty. If it is, then exit

        if snap_list is None:
            return None

        compare_list = []

        if len(snap_list) >= 2:
            range_start = len(snap_list) - 2
            for indx in range(range_start, len(snap_list)):
                compare_list.append(snap_list[indx]["id"])

            # Get the differences between the two snapshots

            old_id = compare_list[0]
            young_id = compare_list[1]

            # Get all of the changes

            try:
                snap_entries = self.connection.snapshot.get_snapshot_tree_diff(young_id, old_id)
            except Exception as excpt:
                if self.logger is not None:
                    self.logger.debug("Error retrieving the snapshot diffs w/ old %d and " + \
                                      "young %d ids, Error was %s.",
                                      old_id, young_id, excpt)
                raise

            # Iterate through the list and get all of the created, modified, and deleted

            (created_list, modified_list, deleted_list, next_page) = \
                self._return_snap_info(snap_entries)

        return (created_list, modified_list, deleted_list, next_page)

    # Compare two snapshots and get the delta differences

    def compare_snapshot(self, name):

        # First, get a list of the snapshots that match our name...

        snap_list = self.find_snapshot(name)
        return self.compare_snapshot_list(snap_list)

    # Find a group of snapshots based upon the snapshot name

    def find_snapshot(self, name):

        # Don't even bother if there is no snapshot name

        if name is None:
            return None

        # Get a list of all of the snapshots and search through them

        try:
            snap_list = self.connection.snapshot.list_snapshots()
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to list snapshots. Error is %s', excpt)
            raise

        # Build a list of the snapshots that match the name

        valid_snaps = []
        snaps = snap_list["entries"]

        for snap in enumerate(snaps):
            if snap[1]["name"] == name:
                valid_snaps.append(snap[1])

        # Return None if the length of the array is zero

        if len(valid_snaps) == 0:
            return None
        else:
            return valid_snaps

    # Create a directory

    def create_dir(self, name, dir_path):

        try:
            self.connection.fs.create_directory(name, dir_path)
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to create directory %s in path %s. Error is %s',
                                  name, dir_path, excpt)
            raise

    # Create a file...
    # You cannot write a file without first creating it.

    def create_file(self, name, data_buffer):

        try:
            dir_info = self.connection.fs.create_file(name, data_buffer)
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to create file %s using API. Error is %s', name, excpt)
            raise

        return dir_info['id']

    # Write a file...
    # The file must first exist before you can write into it
    # Also, the file command actually reads from a file in your filesystem
    # in order to copy the data.

    def write_file(self, fs_id, proc_file):

        try:
            self.connection.fs.write_file(proc_file, id_=fs_id)
        except Exception as excpt:
            if self.logger is not None:
                self.logger.error('Unable to write api file. Error is %s', excpt)
            raise

    # Iterate through a snapshot differences list and get all of the created, modified, and deleted

    def _return_snap_diffs(self, snap_diffs):

        created_list = []
        modified_list = []
        deleted_list = []

        # Find out how many entries that we have and get all of the differences

        for indx in enumerate(snap_diffs):
            if indx[1]["op"] == "CREATE":
                created_list.append(indx[1]["path"])
            elif indx[1]["op"] == "MODIFY":
                modified_list.append(indx[1]["path"])
            else:
                deleted_list.append(indx[1]["path"])

        return (created_list, modified_list, deleted_list)
