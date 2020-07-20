# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from googleapiclient import discovery
from googleapiclient.http import HttpError
import json
import logging
from fabric import Connection
import time
from jq import jq

class InventoryServiceException(Exception):
    """ Exception that is raised if there are any unhandled errors during the call to the GCP API
    """

    def __init__(self, message):
        self.message = message


class InventoryService:
    """Inventory Service that is the entry point to fetching the GCP resources
    This class is work in progress and more methods to access the resources will be added

    Attributes:
        errors: The list of errors encountered during the processsing
        compute_version_id: The compute api version to use. Defaults to v1
        resource_version_id: The cloud resource manager version to use. Defaults to v1
        max_results: The max number of results to fetch in each call to the API. Defaults to 500
        logger: logger handler

    """

    def __init__(self, computeDiscoveryServiceUrl, compute_version_id='v1', resource_version_id='v1', max_results=500):
        """ Initialize the class for the api versions etc..

        Args:
            compute_version_id: The compute api version to use. Defaults to v1
            resource_version_id: The cloud resource manager version to use. Defaults to v1
            max_results: The max number of results to fetch in each call to the API. Defaults to 500
        """

        if computeDiscoveryServiceUrl is None:
            self.compute_service = discovery.build('compute', compute_version_id)
        else:
            self.compute_service = discovery.build('compute', compute_version_id,
                                                   discoveryServiceUrl=computeDiscoveryServiceUrl)

        self.resource_service = discovery.build('cloudresourcemanager', resource_version_id)
        self.max_results = max_results
        self.logger = logging.getLogger(__name__)
        self.errors = []

    def flush_errors(self):
        self.errors = []

    def _execute_(self, request):
        """
        Args:
            request: The Http request object

        Returns:
            A dict with the response
            If there is an HttpError, it will append the error to the errors attribute and return a empty dict

        Raises:
            InventoryServiceException: An exception occurred
        """
        try:
            response = request.execute()
            return response
        except HttpError as httpError:
            message = json.loads(httpError.content)
            self.errors.append(message)
            self.logger.error(message)
            raise InventoryServiceException(message)
        except Exception as ex:
            template = "An exception of type {0} occurred. Details:\n{1!r}"
            message = template.format(type(ex).__name__, ex)
            self.logger.error(message)
            raise InventoryServiceException(message)

    def list_zones(self, project):
        """List the zones for the given project

        Args:
            project: The project id

        Yields:
             The zones for this project

        Raises:
            InventoryServiceException: An exception occurred
        """
        # https://developers.google.com/resources/api-libraries/documentation/compute/v1/python/latest/compute_v1.zones.html#list
        request = self.compute_service.zones().list(project=project, maxResults=self.max_results)
        while request is not None:
            response = self._execute_(request)
            if 'items' in response:
                for item in response['items']:
                    yield item
                request = self.compute_service.zones().list_next(previous_request=request, previous_response=response)
            else:
                return

    def list_projects(self):
        """List the projects that the user has access to.

             Yields:
                  The zones for this project

             Raises:
                 InventoryServiceException: An  exception occurred
        """
        # https://developers.google.com/resources/api-libraries/documentation/cloudresourcemanager/v1/python/latest/cloudresourcemanager_v1.projects.html#list
        request = self.resource_service.projects().list(pageSize=self.max_results)
        while request is not None:
            response = self._execute_(request)
            if 'projects' in response:
                for item in response['projects']:
                    yield item
                request = self.resource_service.projects(). \
                    list_next(previous_request=request, previous_response=response)
            else:
                return

    def list_disks(self, project, zone):
        """List the disks for the given project and zone.

            Args:
                project: The project id
                zone: The zone id

            Yields:
                 The disks for this project

            Raises:
                InventoryServiceException: An exception occurred
        """
        # https://developers.google.com/resources/api-libraries/documentation/compute/v1/python/latest/compute_v1.disks.html#list
        request = self.compute_service.disks().list(project=project, zone=zone, maxResults=self.max_results)
        while request is not None:
            response = self._execute_(request)
            if 'items' in response:
                for item in response['items']:
                    yield item
                request = self.compute_service.disks().list_next(previous_request=request, previous_response=response)
            else:
                return

    def list_regional_disks(self, project, region):
        """List the regional disks for the given project and region.

            Args:
                project: The project id
                region: The region

            Yields:
                 The disks for this project

            Raises:
                InventoryServiceException: An exception occurred
        """
        # https://cloud.google.com/compute/docs/reference/rest/beta/regionDisks
        request = self.compute_service.regionDisks().list(project=project, region=region, maxResults=self.max_results)
        while request is not None:
            response = self._execute_(request)
            if 'items' in response:
                for item in response['items']:
                    yield item
                request = self.compute_service.regionDisks().list_next(previous_request=request,
                                                                       previous_response=response)
            else:
                return

    def list_instances(self, project, zone):
        """List the instances for the given project and zone.

            Args:
                project: The project id
                zone: The zone id

            Yields:
                 The instances for this project

            Raises:
                InventoryServiceException: An exception occurred
        """
        # https://developers.google.com/resources/api-libraries/documentation/compute/v1/python/latest/compute_v1.disks.html#list
        request = self.compute_service.instances().list(project=project, zone=zone, maxResults=self.max_results)
        while request is not None:
            response = self._execute_(request)
            if 'items' in response:
                for item in response['items']:
                    yield item
                request = self.compute_service.disks().list_next(previous_request=request, previous_response=response)
            else:
                return

    def get_instance(self, project, zone, instance):
        """Get the instance object for the given project, zone and instance name

            Args:
                project: The project id
                zone: The zone id
                instance: the instance name

            Yields:
                 The instance object

            Raises:
                InventoryServiceException: An exception occurred
        """
        request = self.compute_service.instances().get(project=project, zone=zone, instance=instance)
        if request is not None:
            response = self._execute_(request)
            return response
        else:
            return None

    def get_zone(self, project, zone):
        """Get the zone object for the given project, zone

            Args:
                project: The project id
                zone: The zone id

            Yields:
                 The zone object

            Raises:
                InventoryServiceException: An exception occurred
        """
        request = self.compute_service.zones().get(project=project, zone=zone)
        if request is not None:
            response = self._execute_(request)
            return response
        else:
            return None

    def attach_disk(self, project, zone, instance, attached_disk_params, force_attach=True):
        """ Attach the disk to the instance

            Args:
                project: The project id
                zone: The zone id
                instance: the instance name
                attached_disk_params : attached_disk_params
                force_attach : force_attach

            Yields:
                 operations

            Raises:
                InventoryServiceException: An exception occurred
        """
        request = self.compute_service.instances().attachDisk(project=project, zone=zone, instance=instance,
                                                              forceAttach=force_attach,
                                                              body=attached_disk_params)
        if request is not None:
            response = self._execute_(request)
            return response
        else:
            return None

    def swap_disks(self, project, primary_instance, primary_zone, standby_instance, standby_zone, user, key_filename,
                   ip_selector=""".[]| select(.name=="nic0")|.accessConfigs[].natIP""",
                   max_attach_retries=10
                   ):
        """Attach the disk to the instance

             Args:
                 project: The project id
                 primary_instance: The primary_instance
                 primary_zone: the primary_zone
                 standby_instance : standby_instance
                 standby_zone : standby_zone
                 user: user to ssh in as
                 key_filename: the key file for the user

             Returns:

             Raises:
                    InventoryServiceException: An exception occurred

            Flow:
            1. Identify the Primary region
            2. Get all regional disks for primary region and keep in "regional_disk" set
               This is needed as there is no tag in the instance that identifies a disk as regional
            3. Get the attatched disk for the primary instance. Skip all the boot and  zonal disks
            4. Force attach to standby instance
            5. ssh into standby instance
            6. mount the drive

            Note that the disk attach expects the device names to be provided as per
            https://medium.com/@DazWilkin/compute-engine-identifying-your-devices-aeae6c01a4d7

            The disks will be mounted at /mnt/disks/<device-name>

            use computeDiscoveryServiceUrl="https://www.googleapis.com/discovery/v1/apis/compute/beta/rest"
            with the InventoryService
        """


        try:
            # Get the region for primary zone
            from_zone_object = self.get_zone(project=project, zone=primary_zone)
            region_uri = from_zone_object['region']
            region = region_uri[region_uri.rindex("/") + 1:]
            regional_disks = self.list_regional_disks(project=project, region=region)

            # Keep  set of the regional disks
            regional_disk_set = set()
            for disk in regional_disks:
                regional_disk_set.add(disk['selfLink'])

            primary_instance_object = self.get_instance(project=project, zone=primary_zone,
                                                                     instance=primary_instance)

            standby_instance_object = self.get_instance(project=project, zone=standby_zone,
                                                                     instance=standby_instance)
            standby_ip = jq(ip_selector).transform(
                standby_instance_object['networkInterfaces'])

            logging.warning("%s %s" % (standby_instance, standby_ip))
            # Get all the disks attatched to the primary instance
            # See https://medium.com/@DazWilkin/compute-engine-identifying-your-devices-aeae6c01a4d7
            # for how to attach disks wth devicename,
            attatched_disks = primary_instance_object['disks']

            with Connection(
                    host=standby_ip,
                    user=user,
                    connect_kwargs={
                        "key_filename": [key_filename,],
                    }) as conn:

                for disk in attatched_disks:
                    # Skip all boot and zonal disks
                    if disk['boot'] is not True and disk['source'] in regional_disk_set:
                        # force attach to standby instance
                        disk_params = dict()
                        disk_params['deviceName'] = disk['deviceName']
                        disk_params['source'] = disk['source']
                        disk_params['mode'] = disk['mode']
                        disk_params['type'] = disk['type']
                        self.attach_disk(project=project, zone=standby_zone, instance=standby_instance,
                                                      attached_disk_params=disk_params, force_attach=True)

                        mkdir_result = conn.run('sudo mkdir -p /mnt/disks/%s' % disk['deviceName'])
                        if mkdir_result.ok:
                            # Loop and wait for the attach to go thru
                            attach_success = False
                            # Sleep fpr 1,2,3,4,5 ....
                            for x in range(0, max_attach_retries):
                                dir = 'test -L /dev/disk/by-id/google-%s' % (disk['deviceName'])
                                dir_result = conn.run(dir, warn=True)
                                if dir_result.failed:
                                    logging.error("Retry %d sleeping for %s seconds " % (x, x))
                                    time.sleep(x)  # x seconds
                                else:
                                    logging.error("success attaching  /dev/disk/by-id/google-%s" % (disk['deviceName']))
                                    attach_success = True
                                    break

                            if not attach_success:
                                raise InventoryServiceException(
                                    "Failed to attach /dev/disk/by-id/google-%s  " % (disk['deviceName']))

                            mount_result = conn.run(
                                "sudo mount -o discard,defaults /dev/disk/by-id/google-%s /mnt/disks/%s" % (
                                    disk['deviceName'], disk['deviceName']))

                            if not mount_result.ok:
                                # TODO: enrich  results
                                raise InventoryServiceException("Failed to run %s " % (mount_result.command))
                        else:
                            # TODO: enrich  results
                            raise InventoryServiceException("Failed to run %s " % (mkdir_result.command))
                        # pp.pprint(result)

        except InventoryServiceException as e:
            logging.error(e.message)

    def list_routes(self, project):
        """List the routes for the given project and zone.

            Args:
                project: The project id

            Yields:
                 The routes for this project

            Raises:
                InventoryServiceException: An exception occurred
        """
        # https://developers.google.com/resources/api-libraries/documentation/compute/v1/python/latest/compute_v1.routes.html
        request = self.compute_service.routes().list(project=project, maxResults=self.max_results)
        while request is not None:
            response = self._execute_(request)
            if 'items' in response:
                for item in response['items']:
                    yield item
                request = self.compute_service.routes().list_next(previous_request=request,
                                                                  previous_response=response)
            else:
                return

    def create_route(self, project, name, priority, network, destination_range, next_hop_gateway):
        """Create the routes.

            Args:
                project: The project id
                name: The name of the route
                priority: The priority for the route (integer)
                network: The network for this route (FQDN)
                destination_range: The cidr that the route is applicable to
                next_hop_gateway: The next hop gateway(FQDN)

            Yields:
                 The response of the created route object

            Raises:
                InventoryServiceException: An exception occurred
        """
        # https://developers.google.com/resources/api-libraries/documentation/compute/v1/python/latest/compute_v1.routes.html

        body = {}

        body["name"] = name
        body["priority"] = priority
        body["network"] = network
        body["destRange"] = destination_range
        body["nextHopGateway"] = next_hop_gateway
        request = self.compute_service.routes().insert(project=project, body=body)
        if request is not None:
            response = self._execute_(request)
            return response

    def delete_route(self, project, route):
        """Delete the routes.

            Args:
                project: The project id
                route: The route name to delete
            Raises:
                InventoryServiceException: An exception occurred
        """
        # https://developers.google.com/resources/api-libraries/documentation/compute/v1/python/latest/compute_v1.routes.html
        request = self.compute_service.routes().delete(project=project, route=route)
        if request is not None:
            response = self._execute_(request)
            return response

